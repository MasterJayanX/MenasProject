from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.



class Cronometro(models.Model):
    ciclos=models.CharField(max_length=10)
    estudio=models.CharField(max_length=10)
    descanso=models.CharField(max_length=10)
    fecha=models.DateTimeField(auto_now=True)