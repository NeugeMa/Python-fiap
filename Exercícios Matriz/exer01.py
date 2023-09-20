# 1. Preencha uma matriz 3x5 com números inteiros informados pelo usuário e exiba a matriz.

# Cria uma matriz vazia com 3 linhas e 5 colunas
matriz = []

# Preenche a matriz com números informados pelo usuário

for i in range(3):
    linha = []
    for j in range(5):
        numero = int(input(f"Digite o número para a posição ({i+1}, {j+1}): "))
        linha.append(numero)
    matriz.append(linha)

# Exibe a matriz

print("Matriz 3x5:")
for linha in matriz:
    for numero in linha:
        print(numero, end="\t")         # \t é usado para separar os números por tabulação
        print()                         # Pula para a próxima linha após exibir uma linha da matriz
