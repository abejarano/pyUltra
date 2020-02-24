import csv, io
from datetime import datetime

from django.contrib import messages
from django.shortcuts import render, redirect

from apps.categorias.models import Nacionalidades, TipoProcesos, Tiendas, Modalidades, Clases
from apps.gestion.models import Tenderos, Denuncias, Productos
from django.core.exceptions import ObjectDoesNotExist


def existeProducto(request, producto):
    try:
        producto = Productos.objects.get(nombre=producto)
        return producto
    except ObjectDoesNotExist:
        messages.add_message(request, messages.WARNING,
                             'En el archivo de importación exísten productos que no están registrados en el '
                             'sistema, por favor realice una importación de productos antes de importar las Denuncias.')
        return False

def existeTendero(request, nombre, apellido):
    try:
        tendero = Tenderos.objects.get(nombre=nombre, apellido=apellido)
        return tendero
    except ObjectDoesNotExist:
        messages.add_message(request, messages.WARNING,
                             'En el archivo de importación exísten tenderos que no están registrados en el '
                             'sistema, por favor realice una importación de tenderos antes de importar las Denuncias.')
        return False

def existeTienda(request, tienda):
    try:
        tienda = Tiendas.objects.get(nombre=tienda)
        return tienda
    except ObjectDoesNotExist:
        messages.add_message(request, messages.WARNING,
                             'En el archivo de importación exísten tiendas que no están registrados en el '
                             'sistema, por favor realice una importación de tiendas antes de importar las Denuncias.')
        return False

def uploadDenuncias(request):
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.add_message(request,messages.WARNING, 'THIS IS NOT A CSV FILE')

    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            tendero = existeTendero(request, column[0], column[1])
            if not tendero:
                break
            producto = existeProducto(request, column[3])
            if not producto:
                break
            tienda = existeTienda(request, column[4])
            if not tienda:
                break
            modalidad, created = Modalidades.objects.get_or_create(nombre=column[5])
            clase, created = Clases.objects.get_or_create(nombre=column[7])
            denuncia = Denuncias.objects.create(
                hechos= column[2],
                fecha_denuncia=datetime.strptime(column[8], '%d/%m/%y %H:%M'),
                estado=column[6],
                tienda=tienda,
                modalidad=modalidad,
                clase=clase
            )
            denuncia.tendero.add(tendero)
            denuncia.producto.add(producto)


    return redirect('/gestion/denuncias/listado', messages)

def uploadTenderos(request):
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        nacionalidad = Nacionalidades.objects.get(nombre=column[2])
        tipo = TipoProcesos.objects.get(nombre=column[7])
        _, created = Tenderos.objects.update_or_create(
            nombre=column[0],
            apellido=column[1],
            nacionalidad=nacionalidad,
            dni=column[3],
            direccion=column[4],
            telefono=column[5],
            sexo=column[6],
            tipo_proceso=tipo,

        )
    
    return redirect('/gestion/tenderos/listado')


def uploadTiendas(request):
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):

        _, created = Tiendas.objects.update_or_create(
            nombre=column[0],
            propietario=column[1],

        )

    return redirect('/gestion/tenderos/listado')

def uploadProductos(request):
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Productos.objects.update_or_create(
            codigo=column[0],
            nombre=column[1],
            monto=column[2],
            area=column[3],
            descripcion=column[4]
        )

    return redirect('/gestion/tenderos/listado')