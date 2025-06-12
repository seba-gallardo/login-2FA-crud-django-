from django import forms
from auth_app.models import Usuario

class UsuarioEditForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido_paterno', 'apellido_materno', 'genero']