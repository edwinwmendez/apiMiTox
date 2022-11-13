from django.db import models


# Create your models here.
class Categoria(models.Model):
    categoria = models.CharField(max_length=100, null=False, blank=False)
    estado = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.categoria


class Frase(models.Model):
    frase = models.CharField(max_length=250, null=False, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    autor = models.CharField(max_length=100, null=True, blank=True)
    significado = models.TextField(null=True, blank=True)
    estado = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.frase + ' - ' + self.autor

