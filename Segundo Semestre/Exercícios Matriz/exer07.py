""" 
7. Preencha uma matriz 5x4 com números informados pelo usuário e exiba a matriz. Em seguida, solicite
um número e faça uma busca na matriz por esse número, informando a posição onde ele se encontra
(índice da linha e índice da coluna). Se o número aparecer mais de uma vez na matriz, exiba todas as
posições onde ele foi encontrado.

"""

from modulo_matriz import preenche_matriz_aleatoria, exibe_matriz 

matriz = preenche_matriz_aleatoria(5, 5)
exibe_matriz(matriz)

numero = int(input('Informe o numero para buscar fna matriz: '))

print()
parar = False
for i in range(len(matriz)): 
    for j in range(len(matriz[0])): 
        if matriz [i][j] == numero: 
            print(f'O {numero} foi encontrado na linha {i} e na coluna {j}')
            break
    if parar == True:
        break 