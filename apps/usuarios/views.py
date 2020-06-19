import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.serializers.json import DjangoJSONEncoder
from django.db import connection
from django.db.models import Count, Func, F, Value, DateField
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from django.utils.timezone import now
from django.views.generic import TemplateView, CreateView, ListView, DeleteView
from requests import Response

from apps.gestion.models import Tenderos, Denuncias
from apps.seguimiento.models import Intervenciones
from apps.usuarios.forms import UserCreateForm
import datetime
from django.http import JsonResponse


def dataGrafico(request):
    now = datetime.datetime.now()
    after = now - datetime.timedelta(days=7)
    after = after.strftime("%Y-%m-%d")
    now = now.strftime("%Y-%m-%d")
    cursor = connection.cursor()

    cursor.execute("select to_char(fecha_denuncia, 'DD-MM-YYYY') as fecha, count(id) as cantidad "
                                "from gestion_denuncias "
                               "WHERE to_char(fecha_denuncia, 'YYYY-MM-DD') BETWEEN '"+after+"' AND '"+now+"' "
                                "GROUP BY to_char(fecha_denuncia, 'DD-MM-YYYY')")

    #cursor.execute("select DATE_FORMAT(fecha_denuncia, '%d-%m-%Y') as fecha, count(id) as cantidad "
    #               "from gestion_denuncias "
    #               "WHERE DATE_FORMAT(fecha_denuncia, '%Y-%m-%d') BETWEEN '" + after + "' AND '" + now + "' "
    #                "GROUP BY DATE_FORMAT(fecha_denuncia, '%d-%m-%Y')")
    columns = [col[0] for col in cursor.description]
    data = {}
    data['Fecha'] = 'Cantidad de casos'
    x = [dict(zip(columns, row))
         for row in cursor.fetchall()
         ]
    for item in x:
        data[item['fecha']] = item['cantidad']


    return JsonResponse(json.loads(json.dumps(dict(data), cls=DjangoJSONEncoder)))

def getTotalData():
    context = {}
    context['total_tenderos'] = Tenderos.objects.count()
    context['total_denuncias'] = Denuncias.objects.count()
    context['total_intervenciones'] = Intervenciones.objects.count()


    return context

def Index(request):
    if request.user.is_authenticated:
        return render(request, 'home.html', getTotalData())
    else:
        if request.method == 'POST':

            if iniciar_sesion(request):
                if request.GET:
                    return HttpResponseRedirect(request.GET.get('next'))
                else:
                    return HttpResponseRedirect('/')
            else:
                messages.warning(request, 'Usuario no está regitrado en el sistema.')
                return HttpResponseRedirect('/')

    return render(request, 'usuarios/login.html')

def iniciar_sesion(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return True
        else:
            return False

def cerrar_sesion(request):
    logout(request)
    return redirect('/')

class Usuario_Registro(CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'usuarios/registrar.html'
    # success_url =

    def form_valid(self, form):
        usuario = form.save(commit=False)
        usuario.save()
        return HttpResponseRedirect('/usuarios/listado')

class Usuario_Listado(ListView):
    model = User
    template_name = 'usuarios/listado.html'
    paginate_by = 20

class Usuario_Eliminar(DeleteView):
    model = User
    template_name = 'usuarios/eliminar.html'
    success_url = '/usuarios/listado'