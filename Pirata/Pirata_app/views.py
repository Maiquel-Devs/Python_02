from django.shortcuts import render

def index(request):
    return render(request, 'index.html')   # Está pegando o arquivo html

def base(request):
    return render(request,'base.html')


# Todo arquivo html, ou melhor todo templates e model tem que passar pela views.py