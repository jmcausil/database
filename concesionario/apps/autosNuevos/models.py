from django.db import models
from apps.autos.models import Autos
# Create your models here.
class Autosnuevos(models.Model):
    unidadesnuevas = models.CharField(max_length=100)
    autos= models.ForeignKey(Autos)


