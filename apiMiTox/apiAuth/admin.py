from django.contrib import admin
from  apiAuth.models import Usuario, CodigoAuth, Unidad


# Register your models here.
# @admin.register(Post)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('unidad', 'usuario')


class UnidadAdmin(admin.ModelAdmin):
    list_display = ('unidad', 'estado')



class CodigoAuthAdmin(admin.ModelAdmin):
    list_display = ('codigo_auth', 'estado')


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Unidad, UnidadAdmin)
admin.site.register(CodigoAuth, CodigoAuthAdmin)