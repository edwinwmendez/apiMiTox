from django.contrib import admin
from frase.models import Frase

# Register your models here.
class FraseAdmin(admin.ModelAdmin):
    list_display = ('frase', 'autor', 'estado')

admin.site.register(Frase, FraseAdmin)

# Register your models here.
