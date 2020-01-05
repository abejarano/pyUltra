from django import forms
from django.forms import FileInput

from .models import Tenderos

class FormTenderos(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields:
            if campo != 'foto':
                self.fields[campo].widget.attrs.update({'required': 'required'})
                self.fields[campo].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Tenderos
        fields = '__all__'
        widgets = {
            'foto':
                FileInput(attrs={'class': 'file-upload',
                                 'accept': 'image/*',
                                 'onchange': 'readURL(this);',
                                 'nombre_etiqueta':'logo'})
        }

