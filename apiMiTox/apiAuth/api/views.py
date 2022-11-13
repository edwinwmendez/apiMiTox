from rest_framework.viewsets import ModelViewSet
from apiAuth.models import Usuario, CodigoAuth, Unidad
from apiAuth.api.serializers import UsuarioSerializer, CodigoAuthSerializer, UnidadSerializer


class UnidadApiViewSet(ModelViewSet):
    serializer_class = UnidadSerializer
    queryset = Unidad.objects.all()

class UsuarioApiViewSet(ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

class CodigoAuthApiViewSet(ModelViewSet):
    serializer_class = CodigoAuthSerializer
    queryset = CodigoAuth.objects.all()
