from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    # Campos de autenticación heredados: username, email, password, etc.
    email = models.EmailField(unique=True)
    
    # Campos personales
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    genero = models.CharField(max_length=10)
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        indexes = [
            models.Index(fields=["-nombre", "-apellido_paterno"], name="idx_apellido_paterno_desc"),
            models.Index(fields=["-nombre", "-apellido_paterno", "-apellido_materno"], name="idx_nombreCompleto_desc"),
            models.Index(fields=["-nombre"], name="idx_nombre_desc")
        ]
    
    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno}"
