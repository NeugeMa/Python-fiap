# 4. Preencha uma matriz 5x5 com números aleatórios e exiba a matriz. A seguir, calcule o somatório dos
# elementos da diagonal principal da matriz.

from modulo_matriz import preenche_matriz_aleatoria, exibe_matriz 

matriz = preenche_matriz_aleatoria(5, 5) 
exibe_matriz(matriz)

soma = 0 
for i in range(matriz(len)): 
    for j in range(len(matriz[0])): 
        if i == j:                  # indice de linha == indice de coluna 
            soma += matriz[i][j]

print(f'Somatorio da diagonal principal: {soma} ')
    
    
""""
    0       1       2
    
0   00      01      02
1   10      11      12
2   20      21      22


"""