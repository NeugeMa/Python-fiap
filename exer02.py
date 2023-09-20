""""
2. Crie uma função chamada calcular_area_retangulo que aceite dois parâmetros:
base e altura, ambos com valores padrão iguais a 1. A função deve retornar a área
do retângulo.
"""

def calcular_area_retangulo(base=1, altura=1):
    area = base * altura
    return area

# Exemplo de uso da função:
area1 = calcular_area_retangulo()  # Usando os valores padrão de base e altura
area2 = calcular_area_retangulo(4, 5)  # Passando valores específicos de base e altura

print(f"Área 1: {area1}")
print(f"Área 2: {area2}")

