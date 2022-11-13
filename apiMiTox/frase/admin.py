from django.contrib import admin
from frase.models import Frase, Categoria


# Register your models here.
class FraseAdmin(admin.ModelAdmin):
    list_display = ('frase', 'autor', 'estado')


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'estado')


admin.site.register(Frase, FraseAdmin)
admin.site.register(Categoria, CategoriaAdmin)

# Register your models here.
