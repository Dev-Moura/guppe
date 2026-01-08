"""
Escopo de variáveis
Dois casos de escopos:

1 - Variáeis Globais:
    - Variáveis globais são reconhecidas, ou seja, seu escopo compreende, too o programa.
2 - Variáveis locais:
    - variáveis lovais são reconhecidas somente no escopo em que foi declaradas

para decladara variaǘeis em python fazemos :

nome_da_variavel = valor

Python é uma linguagem de tipagem fraca/dinamica
"""

numero = 42
# numero = "Geek"

if numero > 10:
    novo = numero + 10
    print(novo)

