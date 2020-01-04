from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *

urlpatterns = [
    path('tenedores/registrar', login_required(TenedoresRegistrar.as_view())),
    path('tenedores/listado', login_required(TenedoresListado.as_view())),

    path('productos/registrar', login_required(ProductosRegistrar.as_view())),
    path('productos/listado', login_required(ProductosListado.as_view())),

    path('denuncias/registrar', login_required(DenunciasRegistrar.as_view())),
    path('denuncias/listado', login_required(DenunciasListado.as_view())),
]