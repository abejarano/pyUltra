from django.views.generic import CreateView, ListView, UpdateView

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