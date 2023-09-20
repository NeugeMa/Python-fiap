""""
5. Defina uma função chamada concatenar_strings que aceite duas strings e um
parâmetro nomeado separador com um valor padrão de espaço. A função deve
retornar as duas strings concatenadas com o separador entre elas.

"""
def concatenar_strings(string1, string2, separador=" "):
    resultado = f"{string1}{separador}{string2}"
    return resultado

# Exemplo de uso da função:
texto1 = "Olá"
texto2 = "mundo"
resultado = concatenar_strings(texto1, texto2)

print(resultado)  # Isso imprimirá "Olá mundo" com espaço entre as duas palavras
