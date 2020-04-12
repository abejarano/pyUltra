from django import forms

from apps.seguimiento.models import Intervenciones


class FormIntervencion(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields:
            self.fields[campo].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Intervenciones
        fields = '__all__'