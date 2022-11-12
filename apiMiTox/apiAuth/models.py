from django.db import models


# Create your models here.
class Autorizacion(models.Model):
    unidad = models.CharField(max_length=50, null=False, blank=False)
    usuario = models.CharField(max_length=255, unique=True, blank=False, null=False)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=100, blank=True, null=True)
    cargo = models.CharField(max_length=50, blank=True, null=True)
    codigo_auth = models.CharField(max_length=25, null=False, blank=False)
    estado = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.unidad
