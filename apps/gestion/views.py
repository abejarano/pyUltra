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


class ProductosRegistrar(CreateView):
    template_name = 'gestion/productos-registrar.html'
    model = Productos
    form_class = FormProductos
    success_url = '/gestion/productos/listado'

class ProductosEditar(UpdateView):
    template_name = 'gestion/productos-registrar.html'
    model = Productos
    form_class = FormProductos
    success_url = '/gestion/productos/listado'

class ProductosEliminar(DeleteView):
    model = Productos
    template_name = 'eliminar.html'
    success_url = '/gestion/productos/listado'

    def get_context_data(self, **kwargs):
        context = super(ProductosEliminar, self).get_context_data(**kwargs)
        context['url_return'] = '/gestion/productos/listado'

        return context

class ProductosListado(ListView):
    model = Productos
    paginate_by = 20
    template_name = 'gestion/productos-listado.html'

    def get_queryset(self, **kwargs):
        queryset = self.model.objects.all()
        if 'buscar' in self.request.GET:
            queryset = queryset.filter(codigo__icontains=self.request.GET['buscar']) | queryset.filter(nombre__icontains=self.request.GET['buscar'])

        return queryset

class DenunciasRegistrar(CreateView):
    model = Denuncias
    form_class = FormDenuncias
    template_name = 'gestion/denuncias-registrar.html'
    success_url = '/gestion/denuncias/listado'

class DenunciasEditar(UpdateView):
    model = Denuncias
    form_class = FormDenuncias
    template_name = 'gestion/denuncias-registrar.html'
    success_url = '/gestion/denuncias/listado'


class DenunciasListado(ListView):
    model = Denuncias
    paginate_by = 20
    template_name = 'gestion/denuncias-listado.html'

class DenunciasEliminar(DeleteView):
    model = Denuncias
    template_name = 'eliminar.html'
    success_url = '/gestion/denuncias/listado'

    def get_context_data(self, **kwargs):
        context = super(DenunciasEliminar, self).get_context_data(**kwargs)
        context['url_return'] = '/gestion/denuncias/listado'

        return context