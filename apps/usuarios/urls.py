from django.urls import path
from .views import *

urlpatterns = [
    path('', Login.as_view()),
    # path('home', Home.as_view()),
    path('registrar', Usuario_Registro.as_view()),
    path('listado', Usuario_Listado.as_view())
]