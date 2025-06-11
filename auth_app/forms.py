
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Usuario')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    nombre = forms.CharField(max_length=100, label='Nombre')
    apellido_paterno = forms.CharField(max_length=100, label='Apellido Paterno')
    apellido_materno = forms.CharField(max_length=100, label='Apellido Materno')
    genero = forms.ChoiceField(
        choices=[
            ('masculino', 'Masculino'),
            ('femenino', 'Femenino'),
            ('otro', 'Otro')
        ],
        label='Género'
    )
    
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'nombre', 'apellido_paterno', 'apellido_materno', 'genero', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.nombre = self.cleaned_data['nombre']
        user.apellido_paterno = self.cleaned_data['apellido_paterno']
        user.apellido_materno = self.cleaned_data['apellido_materno']
        user.genero = self.cleaned_data['genero']
        if commit:
            user.save()
        return user