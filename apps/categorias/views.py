from django.shortcuts import render

# Create your views here.
from .models import *
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import *

class ClasesListado(TemplateView):
    template_name = 'categorias/clases-listado.html'

class ClasesRegistrar(CreateView):
    model = Clases
    template_name = 'categorias/clases-registrar.html'
    success_url = '/categorias/clases/listado'
    form_class = FormClases

    def get_context_data(self, **kwargs):
        context = super(ClasesRegistrar, self).get_context_data(**kwargs)
        context['action'] = 'registrar'

        return context

class ModalidadRegitrar(CreateView):
    model = Modalidades
    form_class = FormModalidades
    success_url = '/categorias/modalidades/listado'
    template_name = 'categorias/modalidad-listado.html'

    def get_context_data(self, **kwargs):
        context = super(ClasesRegistrar, self).get_context_data(**kwargs)
        context['action'] = 'registrar'

        return context

class ModalidadListado(TemplateView):
    template_name = 'categorias/modalidad-registrar.html'

class NacionalidadesListado(TemplateView):
    template_name = 'categorias/nacionalidades-listado.html'

class NacionalidadesRegistrar(TemplateView):
    template_name = 'categorias/nacionalidades-registrar.html'

class SituacionesListado(TemplateView):
    template_name = 'categorias/situaciones-listado.html'

class SituacionesRegistrar(TemplateView):
    template_name = 'categorias/situaciones-registrar.html'

class TiendasListado(TemplateView):
    template_name = 'categorias/tiendas-listado.html'

class TiendasRegistrar(TemplateView):
    template_name = 'categorias/tiendas-registrar.html'

class TipoInvolucaradosListado(TemplateView):
    template_name = 'categorias/tipo_involucrados-listado.html'

class TipoInvolucaradosRegistrar(TemplateView):
    template_name = 'categorias/tipo_involucrados-registrar.html'

class TipoProcesosListado(TemplateView):
    template_name = 'categorias/tipo_procesos-listado.html'

class TipoProcesosRegistrar(TemplateView):
    template_name = 'categorias/tipo_procesos-registrar.html'