from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *

urlpatterns = [
    path('clases/listado', login_required(ClasesListado.as_view())),
    path('clases/registrar', login_required(ClasesRegistrar.as_view())),
    path('clases/<pk>/eliminar', login_required(ClasesEliminar.as_view())),
    path('clases/<pk>/editar', login_required(ClasesEditar.as_view())),

    path('tiendas/listado', login_required(TiendasListado.as_view())),
    path('tiendas/registrar', login_required(TiendasRegistrar.as_view())),
    path('tiendas/<pk>/eliminar', login_required(TiendasEliminar.as_view())),
    path('tiendas/<pk>/editar', login_required(TiendasEditar.as_view())),

    path('situaciones/listado', login_required(SituacionesListado.as_view())),
    path('situaciones/registrar', login_required(SituacionesRegistrar.as_view())),
    path('situaciones/<pk>/eliminar', login_required(SituacionesEliminar.as_view())),
    path('situaciones/<pk>/editar', login_required(SituacionesEditar.as_view())),

    path('modalidades/listado', login_required(ModalidadListado.as_view())),
    path('modalidades/registrar', login_required(ModalidadRegitrar.as_view())),
    path('modalidades/<pk>/eliminar', login_required(ModalidadEliminar.as_view())),
    path('modalidades/<pk>/editar', login_required(ModalidadEditar.as_view())),

    path('nacionalidades/listado', login_required(NacionalidadesListado.as_view())),
    path('nacionalidades/registrar', login_required(NacionalidadesRegistrar.as_view())),
    path('nacionalidades/<pk>/eliminar', login_required(NacionalidadesEliminar.as_view())),
    path('nacionalidades/<pk>/editar', login_required(NacionalidadesEditar.as_view())),

    path('tipo-involucrados/listado', login_required(TipoInvolucaradosListado.as_view())),
    path('tipo-involucrados/registrar', login_required(TipoInvolucaradosRegistrar.as_view())),
    path('tipo-procesos/listado', login_required(TipoProcesosListado.as_view())),
    path('tipo-procesos/registrar', login_required(TipoProcesosRegistrar.as_view())),
]