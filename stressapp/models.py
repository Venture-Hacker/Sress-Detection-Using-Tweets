from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class registration(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    phonenumber=models.CharField(max_length=200,null=True)   
    rpassword=models.CharField(max_length=200,null=True)

class feedback(models.Model):
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    subject=models.CharField(max_length=200,null=True)
    message=models.CharField(max_length=1000,null=True)

class doctormodel(models.Model):
    name=models.CharField(max_length=200,null=True)
    qualification=models.CharField(max_length=200,null=True)
    contact=models.CharField(max_length=200,null=True)
    hospitalname=models.CharField(max_length=200,null=True)
    experience=models.CharField(max_length=200,null=True)
    rate=models.CharField(max_length=200,null=True)
