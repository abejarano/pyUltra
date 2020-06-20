from django import forms
from django.forms import FileInput, Select, SelectMultiple

from .models import Tenderos, Productos, Denuncias
from ..seguimiento.models import Asesores


class FormTenderos(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields:
            if campo != 'foto':
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
            self.fields[campo].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Productos
        fields = '__all__'

class FormDenuncias(forms.ModelForm):
    productos_seleccionados = forms.TextInput()

    class Meta:
        model = Denuncias
        # fields = '__all__'
        exclude = ['fecha_denuncia']



class FormAsesores(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields:
            self.fields[campo].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Asesores
        fields = '__all__'