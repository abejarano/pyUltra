from django.urls import path
from .views import *

urlpatterns = [
    path('clases/listado', ClasesListado.as_view()),
    path('clases/registrar', ClasesRegistrar.as_view()),
    path('modalidades/listado', ModalidadListado.as_view()),
    path('modalidades/registrar', ModalidadRegitrar.as_view()),
    path('nacionalidades/listado', NacionalidadesListado.as_view()),
    path('nacionalidades/registrar', NacionalidadesRegistrar.as_view()),
    path('situaciones/listado', SituacionesListado.as_view()),
    path('situaciones/registrar', SituacionesRegistrar.as_view()),
    path('tiendas/listado', TiendasListado.as_view()),
    path('tiendas/registrar', TiendasRegistrar.as_view()),
    path('tipo-involucrados/listado', TipoInvolucaradosListado.as_view()),
    path('tipo-involucrados/registrar', TipoInvolucaradosRegistrar.as_view()),
    path('tipo-procesos/listado', TipoProcesosListado.as_view()),
    path('tipo-procesos/registrar', TipoProcesosRegistrar.as_view()),
]