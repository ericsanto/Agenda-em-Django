from django.urls import path
from core.views import *



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('cadastro/', UsuarioCreate.as_view() ,name='cadastro'),
]
