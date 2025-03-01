from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from datetime import datetime
from .models import customer,petProdCategory,petProduct,cart,custForm,ordersdetail
from .forms import PetProductForms,RegisterForm,userAuthentication,petProductFormCrud,customerDetailsForm
from django.contrib.auth import authenticate,login,logout
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.conf import settings
import uuid
from paypal.standard.forms import PayPalPaymentsForm
from django.urls import reverse
from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import customerserializer

# Create your views here.
#Function Based View
def show(request):
    #return render(request,"Index.html")
    category=petProdCategory.objects.all()  #retrive all data from model petProdCategory
    products=petProduct.objects.filter(is_deleted=False) 
    context={'category':category,'products':products}
    return render(request,"Home.html",context)
   
    #context={'name':'dog'}
    # return render(request,"Home.html",context)

    #return HttpResponse("Hello students Welcome to Django")
    # context={}
    # context['Greet']='Good Morning'
    # context['Name']='Hello Nikhil !! How are you??'
    # return render(request,"Index.html",context)

    # return render(request,"Index.html",{'Name':'Nikhil','Msg':'How Are You !!','x':10,'y':18})
    # return render(request,"Index.html",{'Name':'Nikhil','Msg':'How Are You !!','x':0,'y':18})
    # return render(request,"Index.html",{'list1':[10,20,30,40]})
    # context={}
    # context['prodList']=['P101','Mobile',60000,'Mobile Device']
    # return render(request,"Index.html",context)

    # dateDetails=datetime.now()
    # return render(request,"Index.html",{'TodayDateDetails':dateDetails})
    
def viewCards(request,id):
    products=petProduct.objects.filter(id=id)
    return render(request,'viewcards.html',{'products':products})

def crud(request):
    if request.method=='POST':
        print("Request Is",request.method)
        custId=request.POST['custid'] 
        custName=request.POST['custname']  
        custEmail=request.POST['custemail'] 
        custContact=request.POST['custcontact']  
        cust=customer.objects.create(customerId=custId,customerName=custName,customerEmail=custEmail,customerContact=custContact)
        cust.save()
        return HttpResponse("Form Data is submitted successfully !!!")
    else:
        print("Request Is",request.method)
        return render(request,"crud_operation.html")

def showdetails(request):
    custdetails=customer.objects.all()
    return render(request,'dashboard.html',{'customerDetails':custdetails})

def deletecust(request,id):
    custdetails=customer.objects.filter(id=id)
    custdetails.delete()
    return redirect('/showalldetails')

def edits(request,id):
    if request.method=="POST":
        print("Request Is",request.method)
        custId=request.POST['custid'] 
        custName=request.POST['custname']  
        custEmail=request.POST['custemail'] 
        custContact=request.POST['custcontact']  
        n=customer.objects.filter(id=id)
        n.update(customerId=custId,customerName=custName,customerEmail=custEmail,customerContact=custContact)
        return redirect('/showalldetails')
    else:
        custdetails=customer.objects.get(id=id)
        return render(request,'edit.html',{'customerDetails':custdetails})

def contact(request):
    return HttpResponse("Contact Us")
def edit(request,rid):
    return HttpResponse("edit id : "+rid)

def register(request):
    # pd=PetProductForms()
    # registerForm=UserCreationForm
    if request.method=='POST':
        registerForm=RegisterForm(request.POST)
        if registerForm.is_valid():
            registerForm.save()
            return redirect('home')
        else:
            return redirect('register')
    else:
        registerForm=RegisterForm()
        return render(request,'Register.html',{'pd':registerForm})

import datetime
def loginuser(request):
    if request.method=="POST":
        uname=request.POST["username"]
        upass=request.POST["password"]
        print(uname)
        print(upass)
        user=authenticate(request,username=uname,password=upass)
        print(user)
        if user is not None:
            login(request,user)
            response=redirect('home')
            request.session['username']=uname
            response.set_cookie('Username',uname)
            response.set_cookie('Time',datetime.datetime.now())
            return response
        else:
            return redirect('loginuser')

    else:
        userForm=userAuthentication()
        return render(request,'loginuser.html',{'userForm':userForm})
        
import random
from django.contrib import messages 
from django.core.mail import send_mail

def forgotpassword(request):
    if request.method == 'POST':
        email= request.POST.get('email')

        users=User.objects.filter(email=email)
        if users.exists():
            user=users.first()
            otp=random.randint(100000,999999)
            request.session['reset_otp']=otp
            request.session['reset_email']=email
            request.session['otp_purpose']="login"

            subject = "Your Password Reset OTP"
            message = f"Dear {user.username},\n\nYour OTP for passsword reset is: {otp}\n\nPlease enter proper OTP to reset password and It will be valid for 5 minute.\n\nBest Regards,\nYour Support Team."

            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )

            return redirect('verifyotp')
        
        else:
            messages.error(request,"Email not found! Please enter a registered email.")
            return render(request,'forgotpassword.html')
    
    return render(request,'forgotpassword.html')
        
def verifyotp(request):
    if request.method == 'POST':
        enterotp=request.POST.get('otp')
        storedotp=request.session.get('reset_otp')
        otppurpose=request.session.get('otp_purpose','')

        if storedotp and enterotp == str(storedotp):
            if otppurpose == 'login':
                return redirect('resetpassword')
            elif otppurpose == 'payment':
                return redirect('paypalsuccess')
            else:
                return redirect('home')
            
        else:
            messages.error(request,'Invalid OTP! Please Try Again.')

    return render(request,'verifyotp.html')
        
def resetpassword(request):
    if request.method == 'POST':
        newpassword=request.POST['new_password']
        confirmpassword=request.POST['confirm_password']
        email=request.session.get('reset_email')

        if newpassword == confirmpassword:
            try:
                user = User.objects.get(email=email)
                user.set_password(newpassword)
                user.save()

                # Clear session data: 
                del request.session['reset_otp']
                del request.session['reset_email']

                messages.success(request,"Password reset successfull! You can login now!")
                return redirect('loginuser')
            
            except User.DoesNotExist:
                messages.error(request,"Something went wrong!! Try Again!!")
                return redirect('forgotpassword')
        else:
            messages.error(request,'Password do not match !! Try Again!!')
            return render(request,'resetpassword.html')
        
    return render(request,'resetpassword.html')

def signout(request):
    logout(request)
    return redirect('home')

def category(request,id):
    print(id)
    category=petProdCategory.objects.all()
    products=petProduct.objects.filter(prodCategory=id)
    return render(request,'Home.html',{'category':category,'products':products})


# decorator: validation on firstname and lastname,email

# view to show add to cart functionality:
@login_required(login_url='loginuser')
def addtocart(request,id):
    userid=request.user.id
    user_details=User.objects.filter(id=userid)

    products=petProduct.objects.filter(id=id)
    print(products)

    p1=Q(pid=products[0])
    p2=Q(uid=user_details[0])

    prod=cart.objects.filter(p1 & p2)

    n=len(prod)
    context={}
    context['products']=products
    if n==1:
        context['msg']="Already added to cart !! Please check in cart."
        return render(request,'viewcards.html',context)
    else:
        addtocartproduct=cart.objects.create(pid=products[0],uid=user_details[0])
        addtocartproduct.save()
        context['success']="Successfully added to cart !!"
        return render(request,'viewcards.html',context)


    # Basic Implementation
    # productid=petProduct.objects.filter(id=id)
    # print(productid)
    # addtocartproduct=cart.objects.create(pid=productid[0])
    # addtocartproduct.save()
    # return HttpResponse("Product Added Successfully!!")

# To show products from cart  
def viewcart(request):
    userid=request.user.id
    print(userid)
    products=cart.objects.filter(uid=userid)
    print(products)
    totalCount = sum(prod.qty for prod in products)
    totalamount=0
    for prod in products:
        totalamount=totalamount+prod.pid.proPrice*prod.qty
    return render(request,'viewcart.html',{'products':products,'totalCount':totalCount,'totalamount':totalamount})

def updateqty(request,qv,id):
    cartqtydetails=cart.objects.filter(id=id)
    print(cartqtydetails)

    if qv=='1':
        totalcartqty=cartqtydetails[0].qty+1
        cartqtydetails.update(qty=totalcartqty)
        
    else:
        if cartqtydetails[0].qty>1:
            totalcartqty=cartqtydetails[0].qty-1
            cartqtydetails.update(qty=totalcartqty)
    return redirect('viewcart')

def searchanything(request):
    if request.method=="POST":
        searchdata=request.POST['search']
        print(searchdata)
        result=petProduct.objects.filter(prodName__icontains=searchdata)
        print(result)
        return render(request,'searchanything.html',{'result':result})
    else:
        return render(request,'searchanything.html')
    
def removeproduct(request,id):
    product=cart.objects.filter(id=id)
    print(product)
    product.delete()
    return redirect('viewcart')

def checkout(request):
    if request.method=='POST':
        custdetailsForm=customerDetailsForm(request.POST)
        if custdetailsForm.is_valid():
            customer=custdetailsForm.save(commit=False)
            customer.user=request.user
            customer.save()
            return redirect('checkoutdetail')
    else:
        custdetailsForm=customerDetailsForm()
        return render(request,'checkout.html',{'pd':custdetailsForm})

def checkoutdetail(request):
    userid=request.user.id
    print(userid)

    products=cart.objects.filter(uid=userid) 
    print(products)

    totalCount = sum(prod.qty for prod in products)

    totalamount=0  
    for prod in products:   
        totalamount=totalamount+prod.pid.proPrice*prod.qty   

    custformdetail=custForm.objects.filter(user=userid)   

    #================ PayPal Code ====================#
    host= request.get_host()

    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': totalamount,
        'item_name': 'petshop',
        'invoice': uuid.uuid4(),
        'currency_code':'USD',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",
        'return_url': f"http://{host}{reverse('paypalsuccess')}",
        'cancel_url': f"http://{host}{reverse('paypalfailed')}",
    }

    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

    #================ PayPal Code End ====================#

    return render(request,'checkoutdetail.html',{'products':products,'totalCount':totalCount,
            'totalamount':totalamount,'custformdetail':custformdetail,'paypalpayment':paypal_payment})


def paypalsuccess(request):
    userid=request.user.id
    print(userid)

    products=cart.objects.filter(uid=userid) 
    print(products)

    totalamount=0  
    for prod in products:   
        totalamount=totalamount+prod.pid.proPrice*prod.qty   
        order=ordersdetail.objects.create(customerName=prod.uid,pet=prod.pid,quantity=prod.qty,totalPrice=totalamount)
        order.save()
        prod.delete()

    orders=ordersdetail.objects.filter(customerName=userid)
    return render(request,'paymentsuccess.html',{'orders':orders})

def orders(request):
    orders=ordersdetail.objects.filter(customerName=request.user.id)
    return render(request,'orders.html',{'orders':orders})

def paypalfailed(request):

    return render(request,'paymentfailed.html')


def addproduct(request):  
    if request.method=='POST':
        petproductForm=petProductFormCrud(request.POST,request.FILES) 
        if petproductForm.is_valid():  
            petproductForm.save()
            return redirect('home') 
        else:
            return redirect('addproduct') 
    else:
        form=petProductFormCrud() 
        return render(request,'addproductcrud.html',{'form':form})
    


def deleteproductcrud(request,id):
    product=petProduct.objects.get(id=id,is_deleted=False)
    product.is_deleted=True
    product.delete_details=timezone.now()
    product.save()
    return redirect('home')

#Class Based View
class SimpleView(View):
    def get(self,request):
        return HttpResponse("Hello")
    def post(self,request):
        return HttpResponse("Hii")

class crudapi(APIView):
    def get(self,request):    #self used then its a class method otherwise its a static method.
        custid=request.data.get('id',None)
        if custid:
            try:
                customer=custForm.objects.get(id=custid)
                custData=customerserializer(customer)
                return Response(custData.data,status=status.HTTP_200_OK)
            except:
                return Response({'Msg':'For this id no data will be available!!'},status=status.HTTP_404_NOT_FOUND)
        else:
            customer=custForm.objects.all()
            print(customer)
            custData=customerserializer(customer,many=True)
            return Response(custData.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        custdetailData=request.data  #Data will be in single Quotes.
        custData=customerserializer(data=custdetailData)
        if custData.is_valid():
            custData.save()
            return Response({'Msg':'Data is successfully stored!!'},status=status.HTTP_200_OK)
        
        return Response({'Msg':'No data will be available!!'},status=status.HTTP_404_NOT_FOUND)
    
    def patch(self,request):
        new_data=request.data
        custid=new_data.get('id',None)
        if custid:
            try:
                custData=custForm.objects.get(id=custid)
                custData=customerserializer(custData,new_data,partial=True)
                if custData.is_valid():
                    custData.save()
                return Response({'Msg':'Data is successfully stored!!'},status=status.HTTP_200_OK)
            except:
                return Response({'Msg':'For this id no data will be available!!'},status=status.HTTP_404_NOT_FOUND)
        return Response({'Msg':'Please provide id'},status=status.HTTP_200_OK)
        
    
    def delete(self,request):
        custid=request.data.get('id',None)
        if custid:
            try:
                customer=custForm.objects.get(id=custid)
                customer.delete()
                return Response({'Msg':'Data is succesfully deleted!!'},status=status.HTTP_200_OK)
            except:
                return Response({'Msg':'For this id no data will be available!!'},status=status.HTTP_404_NOT_FOUND)
            
        return Response({'Msg':'Please provide id'},status=status.HTTP_200_OK)



