"""
Levantando os próprios erros com raise

raise -> Lança execeções

OBS: Oraise nãoo é uma função. É uma palavra reservada, assim como def ou qualquer outra em python.

Para simplificar, pense no raise como sendo útil para que possamos criar nossas prórprias exceções e menssagens
de erro.

A forma geral de utilização é:

raise TipoDoErro('Mensagem de erro')

OBS: O raise, assim como o return, finaliza a função. Ou seja, nada após o raise é executado.
"""

# Exemplo

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError("Texto precisa ser uma string")
    if type(cor) is not str:
        raise TypeError("cor precisa ser uma string")
    print(f'O texto {texto} será impresso na cor {cor}')

colore("geek", 'azul')


# refatorando


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError("Texto precisa ser uma string")
    if type(cor) is not str:
        raise TypeError("cor precisa ser uma string")
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('geek', 'vermelho')