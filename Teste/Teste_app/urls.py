from django.urls import path
from .views import cadastrar_usuario, listar_usuario

urlpatterns = [
    path('', cadastrar_usuario, name='cadastrar_usuario'),  # URL para cadastrar o usuário
    path('listar/', listar_usuario, name='listar_usuario'),  # URL para listar os usuários
]
