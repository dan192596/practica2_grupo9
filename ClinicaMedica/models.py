from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse

#Modelo para el login
class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    phone = models.IntegerField()
    cui = models.IntegerField()


class Cita(models.Model):
    cui = models.IntegerField()
    description = models.TextField()
    sintomas = models.TextField()
    prescripcion = models.TextField()
    fecha = models.DateField()
    hora = models.TimeField()