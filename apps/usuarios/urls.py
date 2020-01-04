from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *

urlpatterns = [
    path('login', iniciar_sesion),
    path('registrar', login_required(Usuario_Registro.as_view())),
    path('listado', login_required(Usuario_Listado.as_view())),
]