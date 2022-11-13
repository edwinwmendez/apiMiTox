"""apiMiTox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from post.api.router import router_post
from apiAuth.api.router import router_auth
from frase.api.router import router_frase


urlpatterns = [
    path('admin/', admin.site.urls),
    path('apiPost/', include(router_post.urls)),
    path('apiAuth/', include(router_auth.urls)),
    path('frases/', include(router_frase.urls)),
]
