from django.db import models


# Create your models here.
class Autorizacion(models.Model):
    unidad = models.CharField(max_length=50, null=False, blank=False)
    usuario = models.CharField(max_length=20, unique=True, blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellidos = models.CharField(max_length=50, blank=True, null=True)
    cargo = models.CharField(max_length=50, blank=True, null=True)
    estado = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.unidad


class CodigoAuth(models.Model):
    usuario = models.ForeignKey(Autorizacion, on_delete=models.CASCADE, null=True, blank=True)
    codigo_auth = models.CharField(max_length=25, null=True, blank=True)
    descripcion = models.CharField(max_length=100, null=True, blank=True)
    estado = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.codigo_auth