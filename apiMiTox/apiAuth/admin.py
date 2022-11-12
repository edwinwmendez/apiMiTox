from django.contrib import admin
from  apiAuth.models import Autorizacion


# Register your models here.
# @admin.register(Post)
class AutorizacionAdmin(admin.ModelAdmin):
    list_display = ('unidad', 'usuario')

admin.site.register(Autorizacion, AutorizacionAdmin)