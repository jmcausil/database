from django.db import models

# Create your models here.
class Mecanicos(models.Model):
     nombres = models.CharField(max_length=100)
     apellidos = models.CharField(max_length=100)
     fechaContrato = models.DateField (max_length=10)
     salario = models.CharField(max_length=100)
     dni = models.CharField(max_length=100)