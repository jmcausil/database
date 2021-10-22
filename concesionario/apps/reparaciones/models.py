from django.db import models

# Create your models here.

class Reparaciones(models.Model):
 fechaReparacion = models.DateField (max_length=10)
 horasReparacion = models.DateTimeField(max_length=10)