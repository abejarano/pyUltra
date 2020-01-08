from django import forms
from django.forms import FileInput, Select, SelectMultiple

from .models import Tenderos, Productos, Denuncias

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

class FormProductos(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields:
            self.fields[campo].widget.attrs.update({'required': 'required'})
            self.fields[campo].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Productos
        fields = '__all__'

class FormDenuncias(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields:
            if campo != 'tendero' and campo != 'producto' and campo != 'tienda' and campo != 'modalidad' and campo != 'clase':
                self.fields[campo].widget.attrs.update({'required': 'required'})
                self.fields[campo].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Denuncias
        # fields = '__all__'
        exclude = ['fecha_denuncia']
        widgets = {
            'tendero':
                SelectMultiple(attrs={'class': 'form-control selectpicker',
                                      'data-live-search': 'true'
                                    }
                                ),
            'producto':
                SelectMultiple(attrs={'class': 'form-control selectpicker',
                                      'data-live-search': 'true'
                                    }
                                ),
            'tienda':
                Select(attrs={'class': 'form-control selectpicker',
                              'data-live-search': 'true'
                              }
                       ),
            'modalidad':
                Select(attrs={'class': 'form-control selectpicker',
                              'data-live-search': 'true'
                              }
                       ),
            'clase':
                Select(attrs={'class': 'form-control selectpicker',
                              'data-live-search': 'true'
                              }
                       ),
        }