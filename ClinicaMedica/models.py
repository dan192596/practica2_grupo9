from django.db import models

# Create your models here.
from django.contrib.auth.models import User

#Modelo para el login
class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    phone = models.IntegerField()

    def __str__(self):
        return self.user.username