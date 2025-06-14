from django.contrib.auth.models import AbstractUser
from django.db import models
import pyotp

class Usuario(AbstractUser):
    # Campos heredados para la autenticacion
    email = models.EmailField(unique=True)
    # Campos personales
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    genero = models.CharField(max_length=10)
    
    # Campos para 2FA
    totp_secret = models.CharField(max_length=32, blank=True, null=True)
    is_2fa_enabled = models.BooleanField(default=False)
    
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
    
    # Genera un secreto TOTP para el usuario
    def generate_totp_secret(self):
        if not self.totp_secret:
            self.totp_secret = pyotp.random_base32()
            self.save()
        return self.totp_secret
    
    # Genera la URL para el código QR
    def get_totp_uri(self):
        if not self.totp_secret:
            self.generate_totp_secret()
        return pyotp.totp.TOTP(self.totp_secret).provisioning_uri(
            name=self.username,
            issuer_name="Tu Aplicación"
        )
    
    # Verifica el código TOTP
    def verify_totp(self, token):
        if not self.totp_secret:
            return False
        totp = pyotp.TOTP(self.totp_secret)
        return totp.verify(token, valid_window=1)