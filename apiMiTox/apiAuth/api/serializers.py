from rest_framework.serializers import ModelSerializer
from apiAuth.models import  Autorizacion, CodigoAuth


class AutorizacionSerializer(ModelSerializer):
    class Meta:
        model = Autorizacion
        fields = ['id', 'unidad', 'usuario', 'nombre', 'apellidos', 'cargo', 'estado']


class CodigoAuthSerializer(ModelSerializer):
    class Meta:
        model = CodigoAuth
        fields = ['id', 'usuario', 'codigo_auth', 'descripcion', 'estado']