# TUPLAS
# Sequencias de itens

# Tuplas sÃ£o ImutÃ¡veis (nÃ£o podem ser modificadas)

# Tuplas sÃ£o delimitadas por parÃªnteses
tupla = (3, 1, 10, 5)

# Tuplas sÃ£o heterogÃªneas (armazena diferente tipos de dado)
tupla = (3, 'abc', 3.5, 6.99, 'dfdfd', 6.99)

print(tupla[0])
print(tupla[1])

# index - retorna o indice de um determinado item
print(tupla.index(6.99))

# count - conta a quantidade de vezes que um item aparece na tupla
print(tupla.count(6.99))

# operador in - busca um item na tupla e retorna True ou False
if 3 in tupla:
    print('Existe')
else:
    print('NÃ£o existe')

# concatenaÃ§Ã£o de tuplas
tupla1 = (1, 2, 3)
tupla2 = (20, 30, 60)
tupla3 = tupla1 + tupla2 + tupla2
print(tupla3)

# concatenaÃ§Ã£o de strings
a = 'paulo'
b = 'vieira'
c = a.title() + ' ' + b.title()
print(c)

def teste(a, b):
    soma = a + b
    subtracao = a - b
    return soma, subtracao

resultado = teste(30, 7)
print(resultado)
print(resultado[0])
print(resultado[1])

# tupla com 1 Ãºnico item (tem uma virgula no final)
tupla = (10,)        
print(tupla)

# list - copia os itens de uma tupla para uma lista
tupla = (4, 5, 6)
lista = list(tupla)
print(lista)

# tuple - copia os itens de uma lista para uma tupla
lista = [10, 20, 30]
tupla = tuple(lista)
print(tupla)

tupla = ('Paulo', 'Marina', 'Fernando')
lista = list(tupla)
lista.sort()
tupla = tuple(lista)
print(tupla)

# cÃ³pia de lista ou de tupla
lista = [1, 2, 3]
lista2 = lista.copy()       # lista2 = lista + []
lista2.append(100)
print(lista)
print(lista2)