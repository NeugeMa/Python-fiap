""""
7. Crie uma função que aceite um parâmetro nomeado itens que seja uma lista de
strings. A função deve imprimir cada item da lista em linhas separadas.
"""

def imprimir_itens(itens):
    for item in itens:
        print(item)

# Exemplo de uso da função:
lista_de_compras = ["Maçã", "Banana", "Laranja", "Pêra"]
imprimir_itens(itens=lista_de_compras)
