from rest_framework.routers import DefaultRouter
from frase.api.views import CategoriaApiViewSet, FraseApiViewSet


router_categoria = DefaultRouter()
router_categoria.register(prefix='categoria', basename='categoria', viewset=CategoriaApiViewSet)

router_frase = DefaultRouter()
router_frase.register(prefix='frase', basename='frase', viewset=FraseApiViewSet)
