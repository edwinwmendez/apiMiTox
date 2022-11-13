from rest_framework.routers import DefaultRouter
from apiAuth.api.views import UsuarioApiViewSet, CodigoAuthApiViewSet


router_auth = DefaultRouter()
router_auth.register(prefix='usuario', basename='usuario', viewset=UsuarioApiViewSet)
router_auth.register(prefix='codigo', basename='codigo', viewset=CodigoAuthApiViewSet)
