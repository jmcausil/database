from django.db import models
from apps.autos.models import Autos
# Create your models here.
class Autosusados(models.Model):
 matricula = models.CharField(max_length=100)
 autos= models.ForeignKey(Autos)
