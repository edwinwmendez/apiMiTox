from rest_framework.serializers import ModelSerializer
from apiAuth.models import  Usuario, CodigoAuth, Unidad


class UnidadSerializer(ModelSerializer):
    class Meta:
        model = Unidad
        fields = ['id', 'unidad', 'estado']

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'unidad', 'usuario', 'nombre', 'apellidos', 'cargo', 'estado']


class CodigoAuthSerializer(ModelSerializer):
    class Meta:
        model = CodigoAuth
        fields = ['id', 'usuario', 'codigo_auth', 'descripcion', 'estado']