from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from .forms import *

class TenderosListado(ListView):
    template_name = 'gestion/tenderos-listado.html'
    paginate_by = 20
    model = Tenderos

    def get_queryset(self, **kwargs):
        queryset = self.model.objects.all()
        if 'buscar' in self.request.GET:
            queryset = queryset.filter(dni__icontains=self.request.GET['buscar']) | queryset.filter(nombre__icontains=self.request.GET['buscar'])

        return queryset

class TenderosRegistrar(CreateView):
    model = Tenderos
    form_class = FormTenderos
    template_name = 'gestion/tenderos-registrar.html'
    success_url = '/gestion/tenderos/listado'

class TenderosEditar(UpdateView):
    model = Tenderos
    form_class = FormTenderos
    template_name = 'gestion/tenderos-registrar.html'
    success_url = '/gestion/tenderos/listado'

class TenderosEliminar(DeleteView):
    model = Tenderos
    template_name = 'eliminar.html'
    success_url = '/categorias/tipo-involucrados/listado'

    def get_context_data(self, **kwargs):
        context = super(TenderosEliminar, self).get_context_data(**kwargs)
        context['url_return'] = '/gestion/tenderos/listado'

        return context


class ProductosRegistrar(TemplateView):
    template_name = 'gestion/productos-registrar.html'

class ProductosListado(TemplateView):
    template_name = 'gestion/productos-listado.html'

class DenunciasRegistrar(TemplateView):
    template_name = 'gestion/denuncias-registrar.html'

class DenunciasListado(TemplateView):
    template_name = 'gestion/denuncias-listado.html'