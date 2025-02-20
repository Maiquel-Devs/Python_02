from django.shortcuts import render
from django.http import HttpResponse


def calculadora_views(request):
    valor_somado = 0  # Definindo valor inicial para a soma

    if request.method == 'POST':  # Certificando-se de que a requisição é POST
        try:
            # Pegando os valores do formulário e convertendo para inteiro
            num1 = int(request.POST.get('soma1', 0))  # Valor padrão 0 se não houver entrada
            num2 = int(request.POST.get('soma2', 0))  # Valor padrão 0 se não houver entrada
            valor_somado = num1 + num2  # Realizando a soma
        except ValueError:
            # Se o valor não for numérico, retornamos um valor 0 ou uma mensagem de erro
            valor_somado = "Por favor, insira números válidos!"

    return render(request, 'index.html', {'Novo_Valor_Somado': valor_somado})

#views.calculadora_views