""""
4. Crie uma função chamada enviar_email que aceite os parâmetros destinatario,
assunto e corpo. O parâmetro assunto deve ter um valor padrão de "Sem assunto".
O parâmetro corpo deve ter um valor padrão de uma string vazia. A função deve
imprimir as informações formatadas. Inclua uma docstring que explique brevemente
o propósito da função.

"""

def enviar_email(destinatario, assunto="Sem assunto", corpo=""):
    """
    Envia um email para o destinatário com o assunto e corpo especificados.

    Parâmetros:
    destinatario (str): O endereço de email do destinatário.
    assunto (str, opcional): O assunto do email (padrão é "Sem assunto").
    corpo (str, opcional): O corpo do email (padrão é uma string vazia).
    """
    print("Enviando email para:", destinatario)
    print("Assunto:", assunto)
    print("Corpo do email:")
    print(corpo)

# Exemplo de uso da função:
enviar_email(destinatario="exemplo@email.com", assunto="Reunião", corpo="Lembre-se da reunião amanhã!")
