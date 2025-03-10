from django.shortcuts import render
from .models import Usuario

def cadastrar_usuario(request):
    if request.method == "POST":
        nome = request.POST['nome']
        senha = request.POST['senha']

        # Salvar os dados no banco de dados
        salvar_dados = Usuario(nome=nome, senha=senha)
        salvar_dados.save()

    return render(request, 'formulario.html')  


def listar_usuario(request):
    dados_usuario = Usuario.objects.all()  
    return render(request, 'listar.html', {'usuario': dados_usuario})

