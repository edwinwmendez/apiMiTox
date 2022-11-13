from django.contrib import admin
from  apiAuth.models import Autorizacion, CodigoAuth


# Register your models here.
# @admin.register(Post)
class AutorizacionAdmin(admin.ModelAdmin):
    list_display = ('unidad', 'usuario')


admin.site.register(Autorizacion, AutorizacionAdmin)


class CodigoAuthAdmin(admin.ModelAdmin):
    list_display = ('codigo_auth', 'estado')


admin.site.register(CodigoAuth, CodigoAuthAdmin)
