"""
Entendendo Iteradores e Iterados

Iterator ->
    - Um objeto que pode ter iterado.
    - um objeto que retorna um dado. sendo um elemento por vez quando uma funçao next() e chamada

Iterable ->
    - um objeto que ira retornar um iterator qunado a funçao iter() for chamada.
"""

nome = 'Geek' # e um iterable mas nao um iterator
numeros = [1, 2, 3, 4, 5, 6] # e um iterable mas nao um iterator

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))

nome = 'Geek'

for letra in nome:
    print('f {letra}')