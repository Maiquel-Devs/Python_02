from django.shortcuts import render, redirect
from .models import Usuario

def cadastrar_usuario(request):
    if request.method == 'Post':
        Pegar_nome = request.POST.get('nome')
        Pegar_senha = request.Post.get('senha')

        # Criar e salvar usuário no banco / Enviando dados no arquivo models
        salvar_usuario = Usuario(nome = Pegar_nome, Senha = Pegar_senha)  # 'nome' e 'senha' no arquivo models
        salvar_usuario.save()

        return redirect('listar_usuarios')
    
    return render(request, 'cadastrar_usuario.html')


def lista_usuario(request):
    dados_usuario = Usuario.objects.all   # essa variavel vai receber todos os dados do banco de dados
    return render(request, 'listar_usuario.html', {'usuario': dados_usuario})








def home(request):
    return render(request, 'home.html')


