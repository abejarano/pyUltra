from django.db import models

# Create your models here.


class Clases(models.Model):
    nombre = models.CharField(max_length=60, null=False, blank=False)

class Tiendas(models.Model):
    nombre = models.CharField(max_length=60, null=False, blank=False)
    propietario = models.CharField(max_length=60, null=False, blank=False)

class Situaciones(models.Model):
    nombre = models.CharField(max_length=60, null=False, blank=False)

class Modalidades(models.Model):
    nombre = models.CharField(max_length=60, null=False, blank=False)

class Nacionalidades(models.Model):
    nombre = models.CharField(max_length=60, null=False, blank=False)

class TipoProcesos(models.Model):
    nombre = models.CharField(max_length=60, null=False, blank=False)

class TipoInvolucrados(models.Model):
    nombre = models.CharField(max_length=60, null=False, blank=False)