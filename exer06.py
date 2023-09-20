""""
6. Crie uma função chamada comprar_produto que aceite dois parâmetros nomeados:
produto e quantidade. O parâmetro produto deve ter um valor padrão de "produto
desconhecido" e o parâmetro quantidade deve ter um valor padrão de 1. A função
deve retornar uma mensagem indicando a compra do produto na quantidade
especificada.

"""

def comprar_produto(produto="produto desconhecido", quantidade=1):
    mensagem = f"Você comprou {quantidade} {produto}."
    return mensagem

# Exemplo de uso da função:
mensagem_compra1 = comprar_produto()  # Usando os valores padrão de produto e quantidade
mensagem_compra2 = comprar_produto(produto="Camiseta", quantidade=3)  # Comprando 3 camisetas

print(mensagem_compra1)
print(mensagem_compra2)


