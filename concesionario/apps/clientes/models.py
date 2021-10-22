from django.db import models
from django.db.models.base import Model

# Create your models here.
class clientes(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    dni = models.CharField(max_length=100)

