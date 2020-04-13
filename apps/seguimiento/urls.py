from django.urls import path

# from apps.seguimiento.views import generate_pdf
from .views import *

urlpatterns = [
    path('intervencion/<pk>/registrar', IntervencionRegistrar.as_view()),
    path('intervencion/<pk_denuncia>/listado', IntervencionListado.as_view()),
    path('intervencion/<pk>/editar', IntervencionEditar.as_view())
]