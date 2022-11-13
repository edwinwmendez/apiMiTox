from rest_framework.viewsets import ModelViewSet
from frase.models import Categoria, Frase
from frase.api.serializers import CategoriaSerializer, FraseSerializer


class CategoriaApiViewSet(ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()


class FraseApiViewSet(ModelViewSet):
    serializer_class = FraseSerializer
    queryset = Frase.objects.all()
