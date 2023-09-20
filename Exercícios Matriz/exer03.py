# 3. Solicite ao usuário 15 valores e armazene em uma matriz 3x5 e exiba a matriz. A seguir, troque todos
# os elementos da matriz que sejam maiores do que 100 pelo valor zero e exiba a matriz novamente.

# Cria uma matriz vazia 3x5
matriz = []

# Solicita ao usuário 15 valores e preenche a matriz
for i in range(3):
    linha = []
    for j in range(5):
        valor = int(input(f"Digite o valor para a posição ({i + 1}, {j + 1}): "))
        linha.append(valor)
    matriz.append(linha)

# Exibe a matriz original
print("Matriz 3x5 Original:")
for linha in matriz:
    for valor in linha:
        print(valor, end="\t")
    print()

# Substitui os valores maiores que 100 por zero
for i in range(3):
    for j in range(5):
        if matriz[i][j] > 100:
            matriz[i][j] = 0

# Exibe a matriz após a substituição
print("\nMatriz 3x5 após a substituição:")
for linha in matriz:
    for valor in linha:
        print(valor, end="\t")
    print()
