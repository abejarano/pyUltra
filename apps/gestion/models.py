from django.db import models
from apps.categorias.models import Tiendas, Nacionalidades, Clases, Modalidades
from django.utils import timezone
# Create your odels here.

class Productos(models.Model):
    codigo = models.CharField(max_length=8, db_index=True,)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    monto = models.DecimalField(max_digits=19, decimal_places=3, null=False, blank=False)
    area = models.CharField(max_length=100,)
    descripcion = models.CharField(max_length=300)

    def __str__(self):
        return self.nombre

class Tenderos(models.Model):
    SEXO = (
        ('M','MASCULINO'),
        ('F', 'FEMENINO'),
        ('O', 'OTROS'),
        ('N', 'NO ESPECIFICAR')
    )
    TIPO = (
        ('I', 'INTERNO'),
        ('E', 'EXTERNO')
    )
    foto = models.FileField(upload_to='avatar/', null=True, blank=True)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    apellido = models.CharField(max_length=100, null=False, blank=False)
    dni = models.CharField(max_length=30, unique=True, db_index=True, null=False, blank=False)
    tipo = models.CharField(max_length=1, choices=TIPO, null=False, blank=False)
    sexo = models.CharField(choices=SEXO,max_length=1, null=False, blank=False)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    direccion = models.TextField(null=True, blank=True)
    nacionalidad = models.ForeignKey(Nacionalidades, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre + ' ' + self.apellido

    class Meta:
        ordering = ['-id']


class Denuncias(models.Model):
    hechos = models.TextField(null=False, blank=False, verbose_name=('Narra los hechos'))
    fecha_denuncia = models.DateTimeField(default=timezone.now,)
    tendero = models.ManyToManyField(Tenderos)
    tienda = models.ForeignKey(Tiendas, related_name='fk_denuncia_tienda', on_delete=models.PROTECT)
    producto = models.ManyToManyField(Productos)
    modalidad = models.ForeignKey(Modalidades, related_name='fk_denuncia_modalidad', on_delete=models.PROTECT)
    clase = models.ForeignKey(Clases, related_name='fk_denuncia_clase', on_delete=models.PROTECT)

    def __str__(self):
        return self.id

    class Meta:
        ordering = ['-id']