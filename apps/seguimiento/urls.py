from django.contrib.auth.decorators import login_required
from django.urls import path

# from apps.seguimiento.views import generate_pdf
from .views import *

urlpatterns = [
    path('intervencion/<pk>/registrar', login_required(IntervencionRegistrar.as_view())),
    path('intervencion/<pk_denuncia>/listado', login_required(IntervencionListado.as_view())),
    path('intervencion/<pk>/editar', login_required(IntervencionEditar.as_view())),
    path('intervencion/<pk>/eliminar', login_required(IntervencionEliminar.as_view())),

    path('intervencion/imprimir/<pk>/', login_required(IntervencionPDF.as_view())),
]