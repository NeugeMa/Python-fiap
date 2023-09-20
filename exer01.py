"""
1.Escreva uma função chamada mostrar_informacoes que aceite três parâmetros
nomeados: nome, idade e cidade. A função deve imprimir uma mensagem
formatada com essas informações.
"""

def mostrar_informacoes(nome, idade, cidade):
    mensagem = f"Nome: {nome}\nIdade: {idade} anos\nCidade: {cidade}"
    print(mensagem)

# Exemplo de uso da função:
mostrar_informacoes(nome="João", idade=30, cidade="São Paulo")
