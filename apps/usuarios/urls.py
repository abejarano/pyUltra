from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *

urlpatterns = [
    path('data', dataGrafico),
    path('registrar', login_required(Usuario_Registro.as_view())),
    path('listado', login_required(Usuario_Listado.as_view())),
    path('<pk>/eliminar', login_required(Usuario_Eliminar.as_view())),

]