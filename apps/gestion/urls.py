from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *

urlpatterns = [
    path('tenderos/registrar', login_required(TenderosRegistrar.as_view())),
    path('tenderos/listado', login_required(TenderosListado.as_view())),
    path('tenderos/<pk>/editar', login_required(TenderosEditar.as_view())),
    path('tenderos/<pk>/eliminar', login_required(TenderosEliminar.as_view())),

    path('productos/registrar', login_required(ProductosRegistrar.as_view())),
    path('productos/listado', login_required(ProductosListado.as_view())),
    path('productos/<pk>/editar', login_required(ProductosEditar.as_view())),
    path('productos/<pk>/eliminar', login_required(ProductosEliminar.as_view())),

    path('denuncias/registrar', login_required(DenunciasRegistrar.as_view())),
    path('denuncias/listado', login_required(DenunciasListado.as_view())),
]