from rest_framework.viewsets import ModelViewSet
from apiAuth.models import Usuario, CodigoAuth
from apiAuth.api.serializers import UsuarioSerializer, CodigoAuthSerializer


class UsuarioApiViewSet(ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

class CodigoAuthApiViewSet(ModelViewSet):
    serializer_class = CodigoAuthSerializer
    queryset = CodigoAuth.objects.all()
