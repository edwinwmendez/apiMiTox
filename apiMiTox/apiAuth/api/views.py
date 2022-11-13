from rest_framework.viewsets import ModelViewSet
from apiAuth.models import Autorizacion, CodigoAuth
from apiAuth.api.serializers import AutorizacionSerializer, CodigoAuthSerializer


class AutorizacionApiViewSet(ModelViewSet):
    serializer_class = AutorizacionSerializer
    queryset = Autorizacion.objects.all()

class CodigoAuthApiViewSet(ModelViewSet):
    serializer_class = CodigoAuthSerializer
    queryset = CodigoAuth.objects.all()
