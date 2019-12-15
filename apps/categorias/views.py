from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class ClasesListado(TemplateView):
    template_name = 'categorias/clases-listado.html'

class ClasesRegistrar(TemplateView):
    template_name = 'categorias/clases-registrar.html'

class ModalidadListado(TemplateView):
    template_name = 'categorias/modalidad-listado.html'

class ModalidadRegitrar(TemplateView):
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