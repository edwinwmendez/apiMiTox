from django.db import models


# Create your models here.
class Unidad(models.Model):
    unidad = models.CharField(max_length=50, null=False, blank=False)
    estado = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.unidad

    class Meta:
        verbose_name = 'Unidad'
        verbose_name_plural = 'Unidades'


class Usuario(models.Model):
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=20, unique=True, blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellidos = models.CharField(max_length=50, blank=True, null=True)
    cargo = models.CharField(max_length=50, blank=True, null=True)
    celular = models.CharField(max_length=20, blank=True, null=True)
    estado = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.usuario

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


class CodigoAuth(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    codigo_auth = models.CharField(max_length=25, null=True, blank=True)
    descripcion = models.CharField(max_length=100, null=True, blank=True)
    estado = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.codigo_auth

    class Meta:
        verbose_name = 'CodigoAuth'
        verbose_name_plural = 'CodigosAuth'
