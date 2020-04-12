from django.urls import path

# from apps.seguimiento.views import generate_pdf
from .views import *

urlpatterns = [
    path('intervencion/registrar', IntervencionRegistrar.as_view())
]