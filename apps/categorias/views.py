from django.shortcuts import render

# Create your views here.
from .models import *
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import *

class ClasesListado(ListView):
    template_name = 'categorias/clases-listado.html'
    paginate_by = 20
    model = Clases

class ClasesEliminar(DeleteView):
    model = Clases
    template_name = 'categorias/clases-eliminar.html'
    success_url = '/categorias/clases/listado'

class ClasesEditar(UpdateView):
    model = Clases
    form_class = FormClases
    template_name = 'categorias/clases-registrar.html'
    success_url = '/categorias/clases/listado'

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
    template_name = 'categorias/modalidad-registrar.html'

class ModalidadEditar(UpdateView):
    model = Modalidades
    form_class = FormModalidades
    success_url = '/categorias/modalidades/listado'
    template_name = 'categorias/modalidad-registrar.html'

class ModalidadListado(ListView):
    paginate_by = 20
    model = Modalidades
    template_name = 'categorias/modalidad-listado.html'

class ModalidadEliminar(DeleteView):
    model = Modalidades
    template_name = 'eliminar.html'
    success_url = '/categorias/modalidades/listado'

    def get_context_data(self, **kwargs):
        context = super(ModalidadEliminar, self).get_context_data(**kwargs)
        context['url_return'] = '/categorias/modalidades/listado'

        return context

class NacionalidadesListado(TemplateView):
    template_name = 'categorias/nacionalidades-listado.html'

class NacionalidadesRegistrar(TemplateView):
    template_name = 'categorias/nacionalidades-registrar.html'

class SituacionesListado(ListView):
    template_name = 'categorias/situaciones-listado.html'
    model = Situaciones
    paginate_by = 20

class SituacionesRegistrar(CreateView):
    model = Situaciones
    form_class = FormSituaciones
    template_name = 'categorias/situaciones-registrar.html'
    success_url = '/categorias/situaciones/listado'

class SituacionesEditar(UpdateView):
    model = Situaciones
    form_class = FormSituaciones
    template_name = 'categorias/situaciones-registrar.html'
    success_url = '/categorias/situaciones/listado'

class SituacionesEliminar(DeleteView):
    model = Situaciones
    template_name = 'eliminar.html'
    success_url = '/categorias/situaciones/listado'

    def get_context_data(self, **kwargs):
        context = super(SituacionesEliminar, self).get_context_data(**kwargs)
        context['url_return'] = '/categorias/situaciones/listado'

        return context

class TiendasListado(ListView):
    template_name = 'categorias/tiendas-listado.html'
    model = Tiendas
    paginate_by = 20

class TiendasRegistrar(CreateView):
    template_name = 'categorias/tiendas-registrar.html'
    form_class = FormTiendas
    success_url = '/categorias/tiendas/listado'

class TiendasEditar(UpdateView):
    model = Tiendas
    template_name = 'categorias/tiendas-registrar.html'
    form_class = FormTiendas
    success_url = '/categorias/tiendas/listado'

class TiendasEliminar(DeleteView):
    model = Tiendas
    template_name = 'eliminar.html'
    success_url = '/categorias/tiendas/listado'

    def get_context_data(self, **kwargs):
        context = super(TiendasEliminar, self).get_context_data(**kwargs)
        context['url_return'] = '/categorias/tiendas/listado'

        return context

class TipoInvolucaradosListado(TemplateView):
    template_name = 'categorias/tipo_involucrados-listado.html'

class TipoInvolucaradosRegistrar(TemplateView):
    template_name = 'categorias/tipo_involucrados-registrar.html'

class TipoProcesosListado(TemplateView):
    template_name = 'categorias/tipo_procesos-listado.html'

class TipoProcesosRegistrar(TemplateView):
    template_name = 'categorias/tipo_procesos-registrar.html'