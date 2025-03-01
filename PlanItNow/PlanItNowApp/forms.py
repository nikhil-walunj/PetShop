from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import petProduct,custForm

class PetProductForms(forms.Form):
    PetProdName=forms.CharField()
    PetProdPrice=forms.DecimalField()
    PetProdDesc=forms.CharField()

class RegisterForm(UserCreationForm):
    password1=forms.CharField(label="Enter password:",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label="Confirm password:",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

        labels={
            'username':'Enter Username:',
            'first_name':'Enter First Name:',
            'last_name':'Enter Last Name:',
            'email':'Enter Email:',
        }

        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }

        # def clean_email(self):
        #     email=self.cleaned_data.get('email')
        
class userAuthentication(AuthenticationForm):
    username=forms.CharField(label="Enter Username:",widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(label="Enter Password:",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','password']


class petProductFormCrud(forms.ModelForm):
    class Meta:
        model=petProduct
        fields=['prodName','proDesc','proPrice','prodImage','prodRating','prodCategory']

    # def clean_prodName(self):
    #     prodName=self.cleaned_data.get('prodName')
    #     if not prodName.isalpha():
    #         raise forms.ValidationError("Product name must be alphabets only.")
    #     return prodName
        

class customerDetailsForm(forms.ModelForm):
    class Meta:
        model=custForm
        fields=['custfullName','custemailId','custphoneNo','custAddress','custcity','pinCode','countryName','additionalNotes']

        labels = {
            'custfullName': 'Full Name',
            'custemailId': 'Email Address',
            'custphoneNo': 'Phone Number',
            'custAddress': 'Address',
            'custcity': 'City',
            'pinCode': 'Pin Code',
            'countryName': 'Country',
            'additionalNotes': 'Additional Notes',
        }
        widgets = {
            'custfullName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter full name'}),
            'custemailId': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email address'}),
            'custphoneNo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'custAddress': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter address'}),
            'custcity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter city'}),
            'pinCode': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter pin code'}),
            'countryName': forms.TextInput(attrs={'class': 'form-control'}),
            'additionalNotes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter additional notes'}),
        }


