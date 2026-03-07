"""
Dictionary Comprehesion

pense no seguinte:

Se quisermos criar uma lista fazemos:

lista = [1, 2, 3, 4]

Se quisermos criar uma tupla fazemos:

tupla = (1, 2, 3, 4)  # 1, 2, 3, 4

Se quisermos criar um set (conjunto)

Conjunto = {1, 2, 3, 4}

Se quisermos criar um dicionário

dicionário = {'a': 1, 'b': 2, 'c': 3, 'd':4}

# Sintaxy

{chave:valor for valor in iterável}
[valor for valor in iterável]
"""

# Exemplos

# numbers =  {'a': 1, 'b': 2, 'c': 3, 'd':4}

# square = {chave: valor ** 2 for chave, valor in numbers.items()}

# print(square)

number = [1, 2, 3, 4, 5]

squares = {valor: valor ** 2 for valor in number}

print(squares)

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

# Exemplos com lógica condicional

numbers = [1, 2, 3, 4, 5]

res =  {num: ('par' if num % 2 == 0 else 'impar') for num in numbers}

print(res)