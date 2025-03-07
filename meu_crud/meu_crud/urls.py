from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuario.urls')),  # URLs do app usuario
    path('', lambda request: redirect('lista_usuarios')),  # Redireciona a raiz para a lista de usuários
]
