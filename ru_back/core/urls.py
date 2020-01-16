from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView,
)

from .views import *

urlpatterns = [
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('', index, name="index"),
    path('login', login, name="login"),
    path('home', home, name="home"),
    path('elements', elements, name="elements"),
    path('consultar', consultar, name="consultar"),
    path('cadastro', cadastro, name="cadastro"),
    path('validacao', validacao, name="validacao"),
    path('base', base, name="base"),
    path('pesquisa', pesquisa, name="pesquisa")
]
