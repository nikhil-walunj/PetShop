from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Create your models here.
    
class pet(models.Model):
    petName=models.CharField(max_length=100)
    petCat=models.CharField(max_length=100)

    def __str__(self):
        return self.petName
    
class petVaccine(models.Model):
    vaccineName=models.CharField(max_length=100)
    pet=models.ManyToManyField(pet)

class petFood(models.Model):
    petFoodId=models.IntegerField()
    petFoodName=models.CharField(max_length=100)
    petFoodPrice=models.DecimalField(max_digits=7,decimal_places=2)
    petFoodDesc=models.TextField(null=True,blank=True)
    price=models.PositiveIntegerField()
    pet=models.ForeignKey(pet,on_delete=models.PROTECT,null=True,blank=True)
    
    def __str__(self):
        return self.petFoodName

class petFoodDetails(models.Model):
    petFood=models.OneToOneField(petFood,on_delete=models.PROTECT)
    company=models.CharField(max_length=100)
    expiryDate=models.DateField()

def validation_Email(value):
    if "@gmail.com" in value:
        return value
    else:
        raise ValidationError("This field accepts mail id of gmail only ")

class customer(models.Model):
    customerId=models.IntegerField()
    customerName=models.CharField(max_length=100)
    customerEmail=models.CharField(max_length=100, validators=[validation_Email])    
    customerContact=models.BigIntegerField(null=True,blank=True)

    def __str__(self):
        return self.customerName

# class customer(models.Model):
#     custId=models.IntegerField()
#     custName=models.CharField(max_length=100)
#     custAddress=models.TextField()
#     custEmail=models.EmailField(max_length=30)
#     custPhoneNo=models.BigIntegerField()
#     custDob=models.DateField()

class petProdCategory(models.Model):
    categroyName=models.CharField(max_length=100)
    categroyDesc=models.TextField()

    def __str__(self):
        return self.categroyName

class petProduct(models.Model):
    prodName=models.CharField(max_length=100)
    proDesc=models.TextField()
    proPrice=models.DecimalField(max_digits=7,decimal_places=2)
    prodImage=models.ImageField(upload_to='images/')
    prodRating=models.DecimalField(max_digits=2,decimal_places=1)
    prodCategory=models.ForeignKey(petProdCategory,on_delete=models.CASCADE,null=True,blank=True)
    is_deleted=models.BooleanField(default=False)
    delete_details=models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.prodName
    
class cart(models.Model):
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column='uid',null=True,blank=True)
    pid=models.ForeignKey(petProduct,on_delete=models.CASCADE,db_column='pid')
    qty=models.IntegerField(default=1)

class custForm(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    custfullName=models.CharField(max_length=30)
    custemailId=models.EmailField()
    custphoneNo=models.CharField(max_length=15)
    custAddress = models.TextField()
    custcity = models.CharField(max_length=100)
    pinCode = models.IntegerField()
    countryName = models.CharField(max_length=100)
    additionalNotes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.custfullName
    
class ordersdetail(models.Model):
    STATUS_CHOICES = [
        ('PENDING','Pending'),
        ('PROCESSING','Processing'),
        ('SHIPPED','Shipped'),
        ('DELIVERED','Delivered'),
        ('CANCELLED','Cancelled'),
    ]

    customerName=models.ForeignKey(User, on_delete=models.CASCADE)
    pet=models.ForeignKey(petProduct,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    orderDate=models.DateTimeField(auto_now_add=True)
    productstatus=models.CharField(max_length=20,choices=STATUS_CHOICES,default='PENDING')
    totalPrice=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f"Order #{self.id} - {self.productstatus}"
    

    