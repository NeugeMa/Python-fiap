"""""
3. Defina uma função chamada soma que aceite dois parâmetros numéricos (a e b) e
retorne a soma desses números. Utilize anotações de tipos para indicar que os
parâmetros e o retorno são do tipo float.
"""

def soma(a: float, b: float) -> float:
    resultado = a + b
    return resultado

# Exemplo de uso da função:
numero1 = 3.5
numero2 = 2.0
resultado = soma(numero1, numero2)

print(f"A soma de {numero1} e {numero2} é igual a {resultado}")
