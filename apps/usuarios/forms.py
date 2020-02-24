from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import EmailInput, TextInput
from django.utils.translation import ugettext_lazy as _

class UserCreateForm(forms.ModelForm):
    """
        Formulario para creación de usuario.
    """
    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username")
        widgets = {
            'first_name':
            TextInput(attrs={
                'class': 'form-control',
                'nombre_etiqueta': _('Full name '),
                'autofocus' : 'on',
                'message' : _('The field name is required')
            }),
            'last_name':
            TextInput(attrs={
                'class': 'form-control',
                'nombre_etiqueta': _('Last name'),
                'message' : _('The field last name is required')
            }),
            'email':
            EmailInput(attrs={
                'class': 'form-control',
                'nombre_etiqueta': _('Email'),
                'message' : _('The field email is required')
            }),
            'username':
            TextInput(attrs={
                'class': 'form-control',
                'nombre_etiqueta': _('User login'),
                'message' : _('The field user login is required')
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields:
            if campo == 'email':
                self.fields[campo].label = _('Email')
            if campo == 'username':
                self.fields[campo].help_text = None

    def clean_password2(self):
        """Validación de contraseñas iguales."""
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            msg = _('Passwords do not match')
            raise forms.ValidationError(msg)
        return password2

    def clean_username(self):
        value = self.cleaned_data.get("username")
        """Validación de usuario existente."""
        number_occurrences = User.objects.filter(username=value).count()
        if number_occurrences > 0:
            raise forms.ValidationError(_('Username already exists, enter a different one'))
        return value


    def save(self, commit=True):
        """Redefinición de método ``save()`` para guardar la contraseña."""
        try:
            user = super(UserCreateForm, self).save(commit=False)
            user.set_password(self.cleaned_data["password1"])
        except ValidationError:
            msg = _('User could not be saved')
            raise forms.ValidationError(msg)
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    """
        Formulario para actualización de usuario.
    """

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username", "is_active")
        widgets = {
            'first_name':
            TextInput(attrs={'class': 'form-control'}),
            'last_name':
            TextInput(attrs={'class': 'form-control'}),
            'email':
            EmailInput(attrs={'class': 'form-control'}),
            'username':
            TextInput(attrs={'class': 'form-control'}),
            'is_active' :forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        """Redefinición  de ``__init__()`` para propiedades adicionales."""
        super().__init__(*args, **kwargs)
        for campo in self.fields:
            if campo == 'email':
                self.fields[campo].label = _('Correo Electrónico')
            if campo == 'username':
                self.fields[campo].help_text = None
            if campo == 'is_active':
                self.fields[campo].help_text = None

