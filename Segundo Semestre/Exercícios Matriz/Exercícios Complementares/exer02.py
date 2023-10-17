"""
2. Implemente um jogo da velha entre 2 jogadores. Utilize uma matriz 3x3 como tabuleiro. A cada rodada, a matriz deve 
ser exibida no terminal exibindo o estado atual do jogo. A cada rodada um dos dois jogadores deve selecionar a posição 
de linha e coluna que deseja marcar (X ou O).

"""
from modulo_matriz import exibe_matriz

matriz = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
jogador = 'X'
acabou = False                               

while not acabou: 
    exibe_matriz(matriz)
    print(f'\nJOGADOR {jogador}')
    linha = int(input('Linha: '))
    coluna = int(input('Coluna: '))

    matriz[linha][coluna] = jogador
