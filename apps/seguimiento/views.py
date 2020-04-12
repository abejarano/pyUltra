from django.views.generic import CreateView

from apps.seguimiento.forms import FormIntervencion
from apps.seguimiento.models import Intervenciones


class IntervencionRegistrar(CreateView):
    model = Intervenciones
    form_class = FormIntervencion
    template_name = 'intervencion/intervencion-registrar.html'
    success_url = '/gestion/denuncias/listado'
