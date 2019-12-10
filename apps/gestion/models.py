from django.db import models

# Create your models here.

class Clases(models.Model):
    nombre = models.CharField(max_length=40, null=False, blank=False)

class Tiendas(models.Model):
    nombre = models.CharField(max_length=100)
    propietario = models.CharField(max_length=100)