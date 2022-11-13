from rest_framework.serializers import ModelSerializer
from apiAuth.models import  Usuario, CodigoAuth


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'unidad', 'usuario', 'nombre', 'apellidos', 'cargo', 'estado']


class CodigoAuthSerializer(ModelSerializer):
    class Meta:
        model = CodigoAuth
        fields = ['id', 'usuario', 'codigo_auth', 'descripcion', 'estado']