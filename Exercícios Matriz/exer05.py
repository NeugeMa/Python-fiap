# 5. Preencha uma matriz 10x10 com números aleatórios e exiba a matriz. A seguir, exiba o somatório dos
# elementos da diagonal secundária da matriz.

from modulo_matriz import preenche_matriz_aleatoria, exibe_matriz 

matriz = preenche_matriz_aleatoria(10, 10)
exibe_matriz(matriz)

soma = 0 
for i in range(len(matriz)):
    for j in range(len(matriz[0])): 
        if i + j == len(matriz) - 1:        # linha + coluna == tamanho - 1
            soma += matriz[i][j]

print(f'Somatorio da diagonal secundária: {soma} ')

""""
    0       1       2
    
0   00      01      02      0+2==2
1   10      11      12      1+1==2
2   20      21      22      2+0==2

"""