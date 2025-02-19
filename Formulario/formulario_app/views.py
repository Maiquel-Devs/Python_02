from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def formulario_view(request):
    nome = ""
    idade = ""
    
    if request.method == "POST":
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')

    return render(request, 'index.html', {'nome': nome, 'idade': idade})
