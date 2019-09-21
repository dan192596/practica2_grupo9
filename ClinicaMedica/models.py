from django.db import models
from django.urls import reverse

# Create your models here.
from django.contrib.auth.models import User

#Modelo para el login
class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    phone = models.IntegerField()
    cui = models.IntegerField()
    type = models.IntegerField()

#Modelo de usuarios doctores
class TypeUser(models.Model):
    nameType = models.CharField(max_length=50)