from rest_framework.serializers import ModelSerializer
from frase.models import Categoria, Frase


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'categoria', 'estado']

class FraseSerializer(ModelSerializer):
    class Meta:
        model = Frase
        fields = ['id', 'frase', 'categoria', 'autor', 'estado']

