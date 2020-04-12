from django.views.generic import CreateView

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
