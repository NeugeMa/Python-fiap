"""
2. Implemente um jogo da velha entre 2 jogadores. Utilize uma matriz 3x3 como tabuleiro. A cada rodada, a matriz deve 
ser exibida no terminal exibindo o estado atual do jogo. A cada rodada um dos dois jogadores deve selecionar a posição 
de linha e coluna que deseja marcar (X ou O).

"""
def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas
    for linha in tabuleiro:
        if all(casa == jogador for casa in linha):
            return True

    # Verificar colunas
    for coluna in range(3):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
            return True

    # Verificar diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)) or \
       all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True

    return False

def jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"

    while True:
        imprimir_tabuleiro(tabuleiro)
        print(f"Jogador {jogador_atual}, é sua vez.")
        linha = int(input("Escolha a linha (0, 1, ou 2): "))
        coluna = int(input("Escolha a coluna (0, 1, ou 2): "))

        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador_atual
            if verificar_vitoria(tabuleiro, jogador_atual):
                imprimir_tabuleiro(tabuleiro)
                print(f"Jogador {jogador_atual} venceu!")
                break
            elif all(casa != " " for linha in tabuleiro for casa in linha):
                imprimir_tabuleiro(tabuleiro)
                print("Empate!")
                break
            jogador_atual = "O" if jogador_atual == "X" else "X"
        else:
            print("Essa posição já está ocupada. Tente novamente.")

if __name__ == "__main__":
    jogo_da_velha()