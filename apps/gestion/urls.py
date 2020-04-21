from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *
from .imports import uploadTenderos, uploadDenuncias, uploadTiendas, uploadProductos

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
    path('denuncias/<pk>/editar', login_required(DenunciasEditar.as_view())),
    path('denuncias/<pk>/eliminar', login_required(DenunciasEliminar.as_view())),

    path('import/tenderos/', login_required(uploadTenderos)),
    path('import/denuncias/', login_required(uploadDenuncias)),
    path('import/tiendas/', login_required(uploadTiendas)),
    path('import/productos/', login_required(uploadProductos)),

    path('asesores/registrar', login_required(AsesoresRegistrar.as_view())),
    path('asesores/listado', login_required(AsesoresListado.as_view())),
    path('asesores/<pk>/editar', login_required(AsesoresEditar.as_view())),
    path('asesores/<pk>/eliminar', login_required(AsesoresEliminar.as_view())),

    #path('imprimir/<pk>/', login_required(ImprimirDenuncia.as_view())),
    path('imprimir/<pk>/', login_required(DenunciaPDF.as_view())),
]