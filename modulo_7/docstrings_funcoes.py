"""
Docstring for modulo_7.docstrings_funcoes

Documentando funções com Docstrings
"""

print(help(print))


def diz_oi():
    " Uma função simples que retorna a string 'Oi!'"
    return 'Oi! '

print(diz_oi())

print(help(diz_oi))

print(diz_oi.__doc__)

def exponencial(numero, potencia=2):
    """
    Docstring for exponencial
    Função que retorna por padrão o quadrado de 'numero' ou 'numero' á 'potência' informada.


    :param numero: numero que desejamos gerar o exponecial
    :param potencia: Potência que queremos gerar o exponencial. Por padrão é 2.
    :return: Retorna o exponencial de 'Numero' por 'potencia'.

    """
    
    return numero ** potencia


