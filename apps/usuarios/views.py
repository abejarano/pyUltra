from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from django.views.generic import TemplateView, CreateView, ListView

from apps.usuarios.forms import UserCreateForm


class Home(TemplateView):
    template_name = 'home.html'

def Index(request):
    if request.user.is_authenticated:
        return render(request, 'base.html')
    else:
        if request.method == 'POST':
            if iniciar_sesion(request):
                if request.GET:
                    return HttpResponseRedirect(request.GET.get('next'))
                else:
                    return render(request, 'base.html')
            else:
                messages.add_message(request, messages.INFO, 'Hello world.')

    return render(request, 'usuarios/login.html')

def iniciar_sesion(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return True
        else:
            return False

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