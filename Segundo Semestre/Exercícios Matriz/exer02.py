# 2. Preencha uma matriz 6x6 com o elemento 1 em todas as posições em que o índice de linha tem valor
# igual ao índice da coluna. Preencha os demais elementos com zero e exiba a matriz.

# Cria uma matriz 6x6 inicializada com zeros
matriz = [[0] * 6 for _ in range(6)]

# Preenche a diagonal principal com 1s
for i in range(6):
    matriz[i][i] = 1

# Exibe a matriz
print("Matriz 6x6:")
for linha in matriz:
    for elemento in linha:
        print(elemento, end="\t")
    print()
