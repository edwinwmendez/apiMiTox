from rest_framework.routers import DefaultRouter
from apiAuth.api.views import AutorizacionApiViewSet


router_auth = DefaultRouter()
router_auth.register(prefix='auth', basename='auth', viewset=AutorizacionApiViewSet)

