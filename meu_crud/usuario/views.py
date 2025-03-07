from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario/lista.html', {'usuarios': usuarios})  # Na Pasta Template

def criar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'usuario/form.html', {'form': form})

def deletar_usuario(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return redirect('lista_usuarios')

