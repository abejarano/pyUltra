import csv, io

from django.contrib import messages
from django.shortcuts import render, redirect

from apps.categorias.models import Nacionalidades, TipoProcesos
from apps.gestion.models import Tenderos


def uploadTeenderos(request):
    # declaring template
    template = 'gestion/denuncias-listado.html'
    data = Tenderos.objects.all()
    # prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be name, email, address,    phone, profile',
        'profiles': data
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
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