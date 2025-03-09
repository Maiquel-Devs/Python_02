from django.db import models


class Usuario(models.Model):                 # Tabela
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)

    def __str__(self):       # Retorna um nome como uma string e não como um código de segurança
        return self.nome    
