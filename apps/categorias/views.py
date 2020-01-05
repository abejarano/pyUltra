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

class NacionalidadesListado(ListView):
    template_name = 'categorias/nacionalidades-listado.html'
    model = Nacionalidades
    paginate_by = 20

class NacionalidadesEliminar(DeleteView):
    model = Nacionalidades
    template_name = 'eliminar.html'
    success_url = '/categorias/nacionalidades/listado'

    def get_context_data(self, **kwargs):
        context = super(NacionalidadesEliminar, self).get_context_data(**kwargs)
        context['url_return'] = '/categorias/nacionalidades/listado'

        return context

class NacionalidadesRegistrar(CreateView):
    template_name = 'categorias/nacionalidades-registrar.html'
    model = Nacionalidades
    form_class = FormNacionalidades
    success_url = '/categorias/nacionalidades/listado'

class NacionalidadesEditar(UpdateView):
    template_name = 'categorias/nacionalidades-registrar.html'
    model = Nacionalidades
    form_class = FormNacionalidades
    success_url = '/categorias/nacionalidades/listado'

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

class TipoProcesosListado(ListView):
    template_name = 'categorias/tipo_procesos-listado.html'
    model = TipoProcesos
    paginate_by = 20

class TipoProcesosRegistrar(CreateView):
    template_name = 'categorias/tipo_procesos-registrar.html'
    form_class = FormTipoProceso
    model = TipoProcesos
    success_url = '/categorias/tipo-procesos/listado'

class TipoProcesosEditar(UpdateView):
    template_name = 'categorias/tipo_procesos-registrar.html'
    form_class = FormTipoProceso
    model = TipoProcesos
    success_url = '/categorias/tipo-procesos/listado'

class TipoProcesosEliminar(DeleteView):
    model = TipoProcesos
    template_name = 'eliminar.html'
    success_url = '/categorias/tipo-procesos/listado'

    def get_context_data(self, **kwargs):
        context = super(TipoProcesosEliminar, self).get_context_data(**kwargs)
        context['url_return'] = '/categorias/tipo-procesos/listado'

        return context