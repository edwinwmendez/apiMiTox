from rest_framework.routers import DefaultRouter
from apiAuth.api.views import AutorizacionApiViewSet, CodigoAuthApiViewSet


router_auth = DefaultRouter()
router_auth.register(prefix='auth', basename='auth', viewset=AutorizacionApiViewSet)
router_auth.register(prefix='codigo', basename='codigo', viewset=CodigoAuthApiViewSet)
