from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'home.html'

class Login(TemplateView):
    template_name = 'usuarios/login.html'

    def post(self, request, *args, **kwargs):
        return redirect('/home')