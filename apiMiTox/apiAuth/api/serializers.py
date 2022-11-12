from rest_framework.serializers import ModelSerializer
from apiAuth.models import  Autorizacion


class AutorizacionSerializer(ModelSerializer):
    class Meta:
        model = Autorizacion
        fields = ['id', 'unidad', 'usuario', 'cargo', 'codigo_auth', 'estado']
