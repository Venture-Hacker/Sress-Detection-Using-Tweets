from unicodedata import name
from django import forms
from .models import *
from django.contrib.auth.models import User

class registeruserform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        widgets={ 
            'password': forms.PasswordInput()
        }   


class registerform(forms.ModelForm):
    class Meta:
        model=registration
        fields=['phonenumber','rpassword']
        widgets={
            'rpassword' :forms.PasswordInput()
        }
        
        
class feedbackform(forms.ModelForm):
    class Meta:
        model=feedback
        fields=('name','email','subject','message')
        widgets={
            'name' :forms.TextInput(attrs={'class' :'form-control'}),
            'email' :forms.TextInput(attrs={'class':'form-control'}),
            'subject' :forms.TextInput(attrs={'class' :'form-control'}),
            'message' :forms.TextInput(attrs={'class' :'form-control'}),
        }

class predictForm(forms.Form):
    name= forms.CharField(max_length=1000)         