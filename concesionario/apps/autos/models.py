from django.db import models
# from apps.mecanicos.models import Mecanicos
from concesionario.apps.clientes.models import Clientes
# from concesionario.apps.mecanicos.models import Mecanicos



# Create your models here.
class Autos(models.Model):
    matricula = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    # mecanicos = models.ManyToManyField(Mecanicos)
    Clientes = models.ForeignKey(Clientes)
   
