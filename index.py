import mysql.connector

def conectar():
    return mysql.connector.connect(host="localhost", user="", password="", database="meu_banco")

def inserir_usuario(nome, senha):
    conexao = conectar()
    conexao.cursor().execute("INSERT INTO usuarios (nome, senha) VALUES (%s, %s)", (nome, senha))
    conexao.commit()
    conexao.close()

def listar_usuarios():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios")
    print(cursor.fetchall())
    conexao.close()


nome = input("Digite o nome: ")
senha = input("Digite a senha: ")


inserir_usuario(nome, senha)

listar_usuarios()
# Exemplo de uso
# inserir_usuario()
# listar_usuarios()
