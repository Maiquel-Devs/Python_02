from django.urls import path
from .views import lista_usuarios, criar_usuario, deletar_usuario

urlpatterns = [
    path('', lista_usuarios, name='lista_usuarios'),  # A URL raiz dentro do app usuarios vai para a lista de usuários
    path('novo/', criar_usuario, name='criar_usuario'),
    path('deletar/<int:id>/', deletar_usuario, name='deletar_usuario'),
]
