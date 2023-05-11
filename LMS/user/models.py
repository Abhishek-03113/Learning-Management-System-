from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.
class account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=12)
    email = models.CharField(max_length=122)
    mobilenumber = models.CharField(max_length=12)
    password =  models.CharField(max_length=45) 
    birthdate = models.DateField()
'''   
class progress(models.Model):
    Time='''