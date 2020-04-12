from django.db import models

# Create your models here.
from apps.categorias.models import TipoProcesos, Situaciones
from apps.gestion.models import Denuncias


class Asesores(models.Model):
    dni = models.CharField(max_length=30, unique=True, db_index=True, null=False, blank=False)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    apellido = models.CharField(max_length=100, null=False, blank=False)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.nombre + ' ' + self.apellido

    class Meta:
        ordering = ['-dni']


class Intervenciones(models.Model):
    sede_policial = models.CharField(max_length=100, null=False, blank=False)
    juez_paz = models.CharField(max_length=100, null=True, blank=True)
    fiscalia = models.CharField(max_length=100, null=True, blank=True)
    fiscalia_superior = models.CharField(max_length=100, null=True, blank=True)
    juezgado_penal = models.CharField(max_length=100, null=True, blank=True)
    reparacion_civil = models.CharField(max_length=100, null=True, blank=True)
    estado_rc = models.CharField(max_length=100, null=True, blank=True)
    empresa = models.CharField(max_length=100, null=False, blank=False)
    ciudad = models.CharField(max_length=100, null=False, blank=False)
    fecha_traslado = models.DateTimeField(null=True, blank=True)
    fecha_legal = models.DateTimeField(null=True, blank=True)
    descripcion = models.TextField(null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    asesores = models.ForeignKey(Asesores, related_name='fk_interncion_acesores', on_delete=models.PROTECT)
    denuncia = models.ForeignKey(Denuncias, related_name='fk_interncion_denuncias', on_delete=models.PROTECT)
    situacion = models.ForeignKey(Situaciones, related_name='fk_interncion_situaciones', on_delete=models.PROTECT)
    tipo_proceso = models.ForeignKey(TipoProcesos, related_name='fk_interncion_tipo_proceso', on_delete=models.PROTECT)

    def __str__(self):
        return self.pk

    class Meta:
        ordering = ['-created_on']
