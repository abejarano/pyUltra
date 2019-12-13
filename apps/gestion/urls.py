from django.urls import path
from .views import *

urlpatterns = [
    path('tenedores/registrar', TenedoresRegistrar.as_view()),
    path('tenedores/listado', TenedoresListado.as_view()),

    path('productos/registrar', ProductosRegistrar.as_view()),
    path('productos/listado', ProductosListado.as_view()),

    path('denuncias/registrar', DenunciasRegistrar.as_view()),
    path('denuncias/listado', DenunciasListado.as_view()),
]