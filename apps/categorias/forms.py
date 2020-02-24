from .models import *
from django import forms

class FormClases(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields:
            self.fields[campo].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Clases
        fields = '__all__'

class FormTiendas(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields:
            self.fields[campo].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Tiendas
        fields = '__all__'


class FormModalidades(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields:
            self.fields[campo].widget.attrs.update({'class' : 'form-control'})

    class Meta:
        model = Modalidades
        fields = ['nombre']


class FormSituaciones(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields:
            self.fields[campo].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Situaciones
        fields = '__all__'

class FormNacionalidades(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields:
            self.fields[campo].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Nacionalidades
        fields = '__all__'

class FormTipoProceso(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields:
            self.fields[campo].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = TipoProcesos
        fields = '__all__'

class FormTipoInvolucrados(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields:
            self.fields[campo].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = TipoInvolucrados
        fields = '__all__'