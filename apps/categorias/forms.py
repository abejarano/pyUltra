from .models import *
from django import forms

class FormClases(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields:
            self.fields[campo].widget.attrs.update({'required': 'required'})
            self.fields[campo].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Clases
        fields = '__all__'

class FormTiendas(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields:
            self.fields[campo].widget.attrs.update({'required': 'required'})
            self.fields[campo].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Tiendas
        fields = '__all__'


class FormModalidades(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields:
            self.fields[campo].widget.attrs.update({'required' : 'required'})
            self.fields[campo].widget.attrs.update({'class' : 'form-control'})

    class Meta:
        model = Modalidades
        fields = ['nombre']