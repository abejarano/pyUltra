from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView, CreateView, ListView

from apps.usuarios.forms import UserCreateForm


class Home(TemplateView):
    template_name = 'home.html'

class Login(TemplateView):
    template_name = 'usuarios/login.html'

    def post(self, request, *args, **kwargs):
        return redirect('/home')


class Usuario_Registro(CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'usuarios/registrar.html'
    # success_url =

    def form_valid(self, form):
        usuario = form.save(commit=False)
        usuario.is_staff = True
        usuario.save()
        return HttpResponseRedirect('/')

class Usuario_Listado(ListView):
    model = User
    template_name = 'usuarios/listado.html'
    paginate_by = 20