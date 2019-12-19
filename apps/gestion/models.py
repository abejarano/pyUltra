from django.db import models
from apps.categorias.models import Tiendas
# Create your odels here.

class Productos(models.Model):
    codigo = models.CharField(max_length=8, db_index=True,)
    noombre = models.CharField(max_length=100, null=False, blank=False)
    monto = models.DecimalField(max_digits=19, decimal_places=3, null=False, blank=False)
    area = models.CharField(max_length=100,)
    descripcion = models.CharField(max_length=300)
    tienda = models.ManyToManyField(Tiendas)