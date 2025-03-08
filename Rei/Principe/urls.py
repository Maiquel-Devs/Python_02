from django.urls import path
from .views import cadastrar_usuario, lista_usuario

urlpatterns = [
    path('', cadastrar_usuario, name = 'cadastrar_usuario'),
    path('listar/', lista_usuario, name= 'lista_usuario')
]