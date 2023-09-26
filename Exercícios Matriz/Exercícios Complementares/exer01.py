"""
1. Preencha uma matriz 5x5 com números aleatórios (de 1 a 25) de forma que nenhum número se repita na matriz, ou seja 
caso o número sorteado já esteja contido na matriz, outro número deve ser sorteado 

"""

import random 
# Inicialize a matriz vazia
matriz = [[0 for _ in range(5)] for _ in range(5)]

# Lista para acompanhar os números já usados
numeros_usados = []

# Preencha a matriz
for i in range(5):
    for j in range(5):
        while True:
            # Gere um número aleatório de 1 a 25
            numero = random.randint(1, 25)
            # Verifique se o número já foi usado
            if numero not in numeros_usados:
                numeros_usados.append(numero)  # Adicione o número à lista de usados
                matriz[i][j] = numero  # Coloque o número na matriz
                break

# Imprima a matriz
for linha in matriz:
    print(linha)