from django.db import models

# Create your models here.


class Clases(models.Model):
    nombre = models.CharField(max_length=60, null=False, blank=False)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['-id']

class Tiendas(models.Model):
    nombre = models.CharField(max_length=60, null=False, blank=False)
    propietario = models.CharField(max_length=60, null=False, blank=False)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['-id']

class Situaciones(models.Model):
    nombre = models.CharField(max_length=60, null=False, blank=False)

    class Meta:
        ordering = ['-id']

class Modalidades(models.Model):
    nombre = models.CharField(max_length=60, null=False, blank=False)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['-id']

class Nacionalidades(models.Model):
    nombre = models.CharField(max_length=60, null=False, blank=False)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['-id']

class TipoProcesos(models.Model):
    nombre = models.CharField(max_length=60, null=False, blank=False)

    class Meta:
        ordering = ['-id']

class TipoInvolucrados(models.Model):
    nombre = models.CharField(max_length=60, null=False, blank=False)

    class Meta:
        ordering = ['-id']