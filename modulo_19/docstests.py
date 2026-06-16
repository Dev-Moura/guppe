"""
Doctests

Doctest são testes que colocamos na dostring das funções/métodos python.

para rodar um teste do doctest:
    python -m doctest -v nome_do_arquivo.py
"""


def soma(a, b):
    """soma dois números
    >>> soma(2, 3)
    5
    """
    return a + b


print(soma(3, 4))


# outro exemplo, aplicando o TDD


def duplicar(valores):
    """duplica os valores em uma lista
    >>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> duplicar([])
    []

    >>> duplicar(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> duplicar([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
