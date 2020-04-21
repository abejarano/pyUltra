import json
from decimal import Decimal

from django.db import IntegrityError, transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView, DetailView
from .forms import *
from .models import DenunciasProducto
from ..seguimiento.models import Asesores


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
    success_url = '/gestion/tenderos/listado'

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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    denuncia = form.save()
                    denuncia.save()
                    DenunciarProductos(denuncia, request.POST.get("productos_seleccionados"))

                    return HttpResponseRedirect(self.success_url)
            except IntegrityError:
                return self.form_invalid(form)

        return render(request, self.template_name, self.form_class)

    def get_context_data(self, **kwargs):
        context = super(DenunciasRegistrar, self).get_context_data(**kwargs)
        context['productos'] = Productos.objects.all()
        return  context

def DenunciarProductos(obj_denuncia, productos_seleccionados):
    for item in json.loads(productos_seleccionados):
        print(item['producto'])
        DenunciasProducto(
            denuncia=obj_denuncia,
            producto=Productos.objects.get(id=item['producto']),
            cantidad=Decimal(item['cantidad'])
        ).save()

class DenunciasEditar(UpdateView):
    model = Denuncias
    form_class = FormDenuncias
    template_name = 'gestion/denuncias-registrar.html'
    success_url = '/gestion/denuncias/listado'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=self.get_object())
        #form = self.form_class(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    denuncia = form.save()
                    denuncia.save()
                    DenunciasProducto.objects.filter(denuncia=denuncia).delete()
                    DenunciarProductos(self.get_object(), request.POST.get("productos_seleccionados"))

                    return HttpResponseRedirect(self.success_url)
            except IntegrityError as excepcion:
                form.add_error(_('Error : %(value)s' % excepcion.__cause__))
                # return self.form_invalid(form)
        print(form)
        return render(request, 'gestion/denuncias-registrar.html', {'form': form})
    
    def get_context_data(self, **kwargs):
        context = super(DenunciasEditar, self).get_context_data(**kwargs)
        context['producto_denunciados'] = DenunciasProducto.objects.filter(denuncia=self.object)
        context['productos'] = Productos.objects.all()
        return context



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


class AsesoresRegistrar(CreateView):
    model = Asesores
    form_class = FormAsesores
    template_name = 'gestion/asesores-registrar.html'
    success_url = '/gestion/asesores/listado'

class AsesoresListado(ListView):
    model = Asesores
    paginate_by = 20
    template_name = 'gestion/asesores-listado.html'

class AsesoresEditar(UpdateView):
    model = Asesores
    form_class = FormAsesores
    template_name = 'gestion/asesores-registrar.html'
    success_url = '/gestion/asesores/listado'

class AsesoresEliminar(DeleteView):
    model = Asesores
    template_name = 'eliminar.html'
    success_url = '/gestion/asesores/listado'

    def get_context_data(self, **kwargs):
        context = super(AsesoresEliminar, self).get_context_data(**kwargs)
        context['url_return'] = '/gestion/asesores/listado'

        return context


class ImprimirDenuncia(DetailView):
    template_name = 'reportes/reporte-denuncia.html'
    model = Denuncias
    context_object_name = 'denuncia'

    def get_context_data(self, **kwargs):
        context = super(ImprimirDenuncia, self).get_context_data(**kwargs)
        context['tenderos'] = self.object.tendero.all()
        context['productos'] = DenunciasProducto.objects.filter(denuncia=self.object)
        return context
