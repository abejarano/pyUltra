from django.conf import settings
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django_weasyprint import WeasyTemplateResponseMixin

from apps.gestion.models import DenunciasProducto
from apps.seguimiento.forms import FormIntervencion
from apps.seguimiento.models import Intervenciones


class IntervencionRegistrar(CreateView):
    model = Intervenciones
    form_class = FormIntervencion
    template_name = 'intervencion/intervencion-registrar.html'
    success_url = '/gestion/denuncias/listado'

    def get_context_data(self, **kwargs):
        context = super(IntervencionRegistrar, self).get_context_data(**kwargs)
        context['denuncia'] = self.kwargs.get('pk')
        return context


class IntervencionListado(ListView):
    model = Intervenciones
    paginate_by = 20
    template_name = 'intervencion/intervencion-listado.html'

    def get_context_data(self, **kwargs):
        context = super(IntervencionListado, self).get_context_data(**kwargs)
        context['denuncia'] = self.kwargs.get('pk_denuncia')
        return context

    def get_queryset(self, *args, **kwargs):
        queryset = Intervenciones.objects.filter(denuncia=self.kwargs.get('pk_denuncia'))

        return queryset

class IntervencionEditar(UpdateView):
    model = Intervenciones
    form_class = FormIntervencion
    template_name = 'intervencion/intervencion-registrar.html'
    success_url = '/gestion/denuncias/listado'

class IntervencionEliminar(DeleteView):
    model = Intervenciones
    template_name = 'eliminar.html'
    success_url = '/gestion/denuncias/listado'

    def get_context_data(self, **kwargs):
        intervencion = Intervenciones.objects.get(pk=self.kwargs.get('pk'))
        context = super(IntervencionEliminar, self).get_context_data(**kwargs)
        context['url_return'] = '/seguimiento/intervencion/'+str(intervencion.denuncia)+'/listado'

        return context

class ImprimirIntervencion(DetailView):
    template_name = 'reportes/reporte-intervencion.html'
    model = Intervenciones
    context_object_name = 'intervencion'

    def get_context_data(self, **kwargs):
        context = super(ImprimirIntervencion, self).get_context_data(**kwargs)
        context['tenderos'] = self.object.denuncia.tendero.all()
        return context

class IntervencionPDF(WeasyTemplateResponseMixin, ImprimirIntervencion):
    pdf_stylesheets = [
        settings.BASE_DIR + '/static/css/style.css',
    ]
    pdf_attachment = False
    pdf_filename = 'intervencion.pdf'