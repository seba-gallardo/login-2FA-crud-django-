from django.contrib import admin
from .models import Usuario
from django.contrib.auth.admin import UserAdmin

# Registrar Usuario usando UserAdmin (para modelos que extienden AbstractUser)
@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    # Personalizar la visualización en la lista
    list_display = ('username', 'email', 'nombre', 'apellido_paterno', 'apellido_materno', 'genero', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'genero')
    search_fields = ('username', 'email', 'nombre', 'apellido_paterno', 'apellido_materno')
    
    # Personalizar los fieldsets para incluir los campos personalizados
    fieldsets = UserAdmin.fieldsets + (
        ('Información Personal', {
            'fields': ('nombre', 'apellido_paterno', 'apellido_materno', 'genero')
        }),
    )
    
    # Para el formulario de agregar usuario
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Información Personal', {
            'fields': ('email', 'nombre', 'apellido_paterno', 'apellido_materno', 'genero')
        }),
    )
