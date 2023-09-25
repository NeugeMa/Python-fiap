""""
Sistema de Reservas de Passagens Aéreas

Crie um programa que simule um sistema de reservas de passagens aéreas.

Use um dicionário para representar os voos disponíveis, onde as chaves são os números de voo e os valores são
listas contendo informações como origem, destino, quantidade de assentos disponíveis, data e horário.

O programa deve permitir exibir voos disponíveis, verificar a disponibilidade de assentos em um voo específico,
reservar assentos de um voo específico e exibir todos os voos saindo de uma determinada origem.
"""

# Dicionário de voos disponíveis
viagens = {
'A2345': ['São Paulo', 'Rio de Janeiro', 45, '30-08-2023', '18:00'],
'A1873': ['Brasília', 'São Paulo', 20, '30-08-2023', '22:45'],
'Y4430': ['Salvador', 'Goiânia', 60, '03-09-2023', '08:30'],
'F9834': ['São Paulo', 'Florianópolis', 40, '02-09-2023', '10:00'],
'B6789': ['Fortaleza', 'Recife', 30, '04-09-2023', '14:15'],
'C4567': ['Belo Horizonte', 'Curitiba', 50, '05-09-2023', '16:30'],
'D7890': ['Porto Alegre', 'Manaus', 25, '06-09-2023', '20:45'],
'E1234': ['Natal', 'João Pessoa', 35, '07-09-2023', '12:00'],
'G5678': ['Vitória', 'Campo Grande', 55, '08-09-2023', '09:15'],
'H3456': ['Teresina', 'Maceió', 40, '09-09-2023', '19:30'],
'I8901': ['Cuiabá', 'Aracaju', 30, '10-09-2023', '11:45'],
'J2345': ['Palmas', 'Porto Velho', 25, '11-09-2023', '13:30'],
'K7890': ['Boa Vista', 'Rio Branco', 20, '12-09-2023', '17:00'],
'L1234': ['São Luís', 'Belém', 35, '13-09-2023', '15:45'],
'M4567': ['Macapá', 'Rio de Janeiro', 40, '14-09-2023', '08:30'],
'N2345': ['Florianópolis', 'Goiânia', 30, '15-09-2023', '10:15'],
'O8901': ['Porto Alegre', 'Recife', 45, '16-09-2023', '22:00'],
'P5678': ['Curitiba', 'São Paulo', 35, '17-09-2023', '20:45'],
'Q1234': ['Manaus', 'Natal', 25, '18-09-2023', '16:30'],
'R7890': ['João Pessoa', 'Belo Horizonte', 30, '19-09-2023', '14:15'],
'S2345': ['Campo Grande', 'Vitória', 40, '20-09-2023', '12:00']
}

# Função para exibir voos disponíveis
def exibir_voos_disponiveis():
    print("Voos Disponíveis:")
    for voo, info in viagens.items():
        origem, destino, assentos, data, horario = info
        print(f'{voo} - De {origem} para {destino} em {data}, {horario}. Assentos disponíveis: {assentos}')

# Função para verificar disponibilidade de assentos em um voo específico
def verificar_disponibilidade(voo):
    if voo in viagens:
        assentos_disponiveis = viagens[voo][2]
        print(f'Assentos disponíveis no voo {voo}: {assentos_disponiveis}')
    else:
        print(f'Voo {voo} não encontrado.')

# Função para reservar assentos de um voo específico
def reservar_assentos(voo, quantidade):
    if voo in viagens:
        assentos_disponiveis = viagens[voo][2]
        if assentos_disponiveis >= quantidade:
            viagens[voo][2] -= quantidade
            print(f'{quantidade} assentos reservados com sucesso no voo {voo}.')
        else:
            print(f'Não há assentos suficientes disponíveis no voo {voo}.')
    else:
        print(f'Voo {voo} não encontrado.')


# Função para exibir voos saindo de uma determinada origem
def voos_saindo_de(origem):
    print(f'Voos saindo de {origem}:')
    origem = origem.lower()  # Converter a origem do usuário para minúsculas
    for voo, info in viagens.items():
        if info[0].lower() == origem or info[0] == origem:  # Comparar tanto em minúsculas quanto em maiúsculas
            destino = info[1]
            data = info[3]
            horario = info[4]
            print(f'{voo} - Para {destino} em {data}, {horario}')

# Loop principal
while True:
    print("\nMenu:")
    print("1 - Exibir voos disponíveis")
    print("2 - Verificar disponibilidade de assentos em um voo")
    print("3 - Reservar assentos em um voo")
    print("4 - Exibir voos saindo de uma origem")
    print("5 - Encerrar programa")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == '1':
        exibir_voos_disponiveis()
    elif escolha == '2':
        voo = input("Digite o número do voo: ").upper()  # Converter para maiúsculas
        verificar_disponibilidade(voo)
    elif escolha == '3':
        voo = input("Digite o número do voo: ").upper()  # Converter para maiúsculas
        quantidade = int(input("Digite a quantidade de assentos a reservar: "))
        reservar_assentos(voo, quantidade)
    elif escolha == '4':
        origem = input("Digite a origem dos voos desejados: ")
        voos_saindo_de(origem) 
    elif escolha == '5':
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")







