from django.contrib import admin
from  apiAuth.models import Usuario, CodigoAuth


# Register your models here.
# @admin.register(Post)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('unidad', 'usuario')


admin.site.register(Usuario, UsuarioAdmin)


class CodigoAuthAdmin(admin.ModelAdmin):
    list_display = ('codigo_auth', 'estado')


admin.site.register(CodigoAuth, CodigoAuthAdmin)
