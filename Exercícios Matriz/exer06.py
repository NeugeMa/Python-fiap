# 6. Preencha uma matriz 5x5 com números aleatórios e exiba a matriz. A seguir, informe o 
# menor elemento da matriz.

from modulo_matriz import preenche_matriz_aleatoria, exibe_matriz 

matriz = preenche_matriz_aleatoria(5, 5)
exibe_matriz(matriz)

menor = matriz[0][0]
linha_menor = 0 
coluna_menor = 0 

for i in range(len(matriz)):
    for j in range(len(matriz[0])): 
        if matriz[i][j] < menor: 
            menor = matriz[i][j]
            linha_menor = i 
            coluna_menor = j 
        
print(f'O menor valor é {menor} e está na linha {linha_menor} e coluna {coluna_menor}')