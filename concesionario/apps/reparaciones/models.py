from django.db import models

from concesionario.apps.autos.models import Autos
from concesionario.apps.mecanicos.models import Mecanicos

# Create your models here.

class Reparaciones(models.Model):
 fechaReparacion = models.DateField (max_length=10)
 horasReparacion = models.DateTimeField(max_length=10)
 Autos = models.ForeignKey(Autos)
 mecanicos = models.ForeignKey(Mecanicos)