from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
 

class Login(models.Model):
    name=models.CharField(max_length=16)
    password=models.CharField(max_length=100)
    fecha=models.DateTimeField(auto_now=True)

