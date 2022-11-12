from rest_framework.viewsets import ModelViewSet
from apiAuth.models import Autorizacion
from apiAuth.api.serializers import AutorizacionSerializer


class AutorizacionApiViewSet(ModelViewSet):
    serializer_class = AutorizacionSerializer
    queryset = Autorizacion.objects.all()
