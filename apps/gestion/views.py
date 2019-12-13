from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class TenedoresListado(TemplateView):
    template_name = 'gestion/tenedores-listado.html'

class TenedoresRegistrar(TemplateView):
    template_name = 'gestion/tenedores-registrar.html'

class ProductosRegistrar(TemplateView):
    template_name = 'gestion/productos-registrar.html'

class ProductosListado(TemplateView):
    template_name = 'gestion/productos-listado.html'

class DenunciasRegistrar(TemplateView):
    template_name = 'gestion/denuncias-registrar.html'

class DenunciasListado(TemplateView):
    template_name = 'gestion/denuncias-listado.html'