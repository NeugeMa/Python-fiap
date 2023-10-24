''''
RM 550494 - Mariana Neugebauer Dourado
RM 552295 - Matheus Felipe Camarinha Duarte
RM 550167 - Vinicius de Alencar Chagas
'''

import random

"""
Explicação do código;
Iniciando o código na linha: 150 
    Começamos com um laço de repetição para sempre continuar rodando 
        (só irá parar, caso o usuário digite 0)

Código linha 29
Após nós criamos uma lista de cartelas, para dar inicío a lista de nome de jogadores
    Depois declaramos que "venceu" como false para o laço de baixo rodar até que um jogador vença e junto disso é 
    decidido uma lista vazia com números que podem ser sorteados. 

Código linha 48 à 74
    Já no começo do laço é exibido todas as tabelas uma em cima da outra, após isso o jogador irá ficar apertando enter
    para criar um novo número sorteado.
        - A lista de números vai para a função de sortear para não cair o mesmo número. 

Código linha 104
    Após tudo isso, é retornado o nome do ganhador, e se ninguém ganhou fica vazio, logo não estará na lista de jogadores, 
    mas se caso ele esteja definimos ele como True e o laço para. 
"""
def definir_jogadores():    # definição de jogadores 
    while True:
        try: #verificando se o número de jogadores é válido e se é um número
            qtd = int(input("Digite quantos jogadores irão participar (digite 0 para encerrar): "))
            if 0 <= qtd <= 5:
                break
            else:
                print("Número de jogadores inválido, escolha entre 0 e 5"),02
        except ValueError:
            print("Por favor, insira um número válido.")
    if qtd == 0:
        return 0
    lista_jogadores = []
    while len(lista_jogadores) < qtd:
        nome = input(f'Digite o nome do Jogador: ')
        nome = nome.replace(" ","-")
        print(nome)
        lista_jogadores.append(nome)
    return lista_jogadores

def criar_cartelas(lista_jogadores):        #criando cartelas pra cada jogador
    lista_cartelas = {}
    for pessoa in lista_jogadores:
        pre_cartela = []
        for i in range(5):
            minimo = (i*10)+1
            maximo = (i+1)*10
            linha = []
            while len(linha) < 5: 
                n = random.randint(minimo,maximo)
                if n <10 and n > 0:
                    n = (f'0{n}')
                if str(n) not in linha:
                    linha.append(str(n))
            pre_cartela.append(linha)
        cartela = []
        for i in range(len(pre_cartela[0])):
            linha = []
            for j in range(len(pre_cartela)):
                linha.append(0)
            cartela.append(linha)
        for k in range(5):
            for j in range(5):
                cartela[k][j] = pre_cartela[j][k]
        lista_cartelas[pessoa] = cartela
    return lista_cartelas

def exibir_cartelas(lista_cartelas, jogadores):                      #exibindo as cartelas
    for jogador in jogadores:
        cartela_atual = lista_cartelas[jogador]
        print(jogador.replace("-"," "))
        topo_fim = "+----------------+"
        print(topo_fim)
        
        for i in range(len(cartela_atual)):
            print("| ", end="")
            for j in range(len(cartela_atual[0])):
                print(cartela_atual[i][j], end=' ')
            print("|", end="\n")
        print(topo_fim+'\n')

def sortear_numero(numeros_sorteados):                       #sorteando os números
    sorteio_valido = False
    while sorteio_valido == False:
        numero = random.randint(1,50)
        if numero not in numeros_sorteados:
            sorteio_valido = True
    return numero

def verificar_cartelas(lista_cartelas, numero_sorteado, jogadores):
    if numero_sorteado > 0 and numero_sorteado <10:
        numero_sorteado = (f'0{numero_sorteado}')
    for jogador in jogadores:
        cartela_atual = lista_cartelas[jogador]
        for i in range(len(cartela_atual)):
            for j in range(len(cartela_atual[0])):
                if cartela_atual[i][j] == str(numero_sorteado):
                    cartela_atual[i][j] = "XX"
    return lista_cartelas

def verificar_ganhadores(lista_cartelas, lista_jogadores):                 #verificando se tem ganhadores
    ganhador = ""
    for jogador in lista_jogadores:
        c_a = lista_cartelas[jogador]
        if ((c_a[0][0] == c_a[0][1] == c_a[0][2] == c_a[0][3] == c_a[0][4]) or
            (c_a[1][0] == c_a[1][1] == c_a[1][2] == c_a[1][3] == c_a[1][4]) or
            (c_a[2][0] == c_a[2][1] == c_a[2][2] == c_a[2][3] == c_a[2][4]) or
            (c_a[3][0] == c_a[3][1] == c_a[3][2] == c_a[3][3] == c_a[3][4]) or
            (c_a[4][0] == c_a[4][1] == c_a[4][2] == c_a[4][3] == c_a[4][4]) or
            (c_a[0][0] == c_a[1][0] == c_a[2][0] == c_a[3][0] == c_a[4][0]) or
            (c_a[0][1] == c_a[1][1] == c_a[2][1] == c_a[3][1] == c_a[4][1]) or
            (c_a[0][2] == c_a[1][2] == c_a[2][2] == c_a[3][2] == c_a[4][2]) or
            (c_a[0][3] == c_a[1][3] == c_a[2][3] == c_a[3][3] == c_a[4][3]) or
            (c_a[0][4] == c_a[1][4] == c_a[2][4] == c_a[3][4] == c_a[4][4]) or        
            (c_a[0][0] == c_a[1][1] == c_a[2][2] == c_a[3][3] == c_a[4][4]) or
            (c_a[0][4] == c_a[1][3] == c_a[2][2] == c_a[3][1] == c_a[4][0])):
            ganhador = jogador
            ganhador_formatado = ganhador.replace("-"," ")
            exibir_cartelas(lista_cartelas, lista_jogadores)
            print(f"Parabéns, o vencedor desta rodada é: {ganhador_formatado}")
    return ganhador

def controlar_ranking(ganhador, demais):
    demais.remove(ganhador)
    try:
        with open('ranking.txt', 'r') as arquivo:
            nomes_ranking = set()
            novas_linhas = []
            for linha in arquivo:
                # Verifica se a linha não está vazia antes de tentar dividi-la
                if linha.strip():  # Remove espaços em branco e verifica se a linha não está vazia
                    nome, vitorias = linha.split()
                    nomes_ranking.add(nome)
                    if ganhador == nome:
                        vitorias = int(vitorias)
                        vitorias += 1
                    new_line = (f'{nome} {int(vitorias)}')
                    novas_linhas.append(new_line)
            if ganhador not in nomes_ranking:
                novas_linhas.append(f'{ganhador} 1')
            if len(demais) != 0:
                for i in demais:
                    if i not in nomes_ranking:
                        novas_linhas.append(f'{i} 0')
        with open('ranking.txt', 'w') as arquivo:
            for pessoa in novas_linhas:
                arquivo.write(pessoa + '\n')
    except FileNotFoundError:
        with open('ranking.txt', 'w') as arquivo:
            arquivo.write(ganhador + ' 1')
            if len(demais) != 0:
                for i in demais:
                    arquivo.write(i + ' 0')

def exibir_ranking():
    print()
    with open('ranking.txt', 'r') as arquivo:
        for linha in arquivo:
            print(linha.replace("-"," "), end='')
    print()

# o comando em si, sem serem as funções, começam aqui:
while True:
    lista_jogadores = definir_jogadores()
    if lista_jogadores == 0 :
        print("fim do programa!")
        break
    lista_cartelas = criar_cartelas(lista_jogadores)
    venceu = False
    numeros_sorteados = []
    numero = ""
    while venceu == False:
        exibir_cartelas(lista_cartelas, lista_jogadores)
        print(f'O número sorteado nesta rodada: {numero}')
        input("Digite enter para sortear um número\n ")
        numero = sortear_numero(numeros_sorteados)
        numeros_sorteados.append(numero)
        print(f'O número sorteado é: {numero}')
        lista_cartelas = verificar_cartelas(lista_cartelas, numero, lista_jogadores)
        ganhador = verificar_ganhadores(lista_cartelas, lista_jogadores)
        if ganhador in lista_jogadores:
            venceu = True
    controlar_ranking(ganhador, lista_jogadores)
    exibir_ranking()