"""
Reversed

OBS: Não confunda com a função reverse() que estudamos nas listas.

A função reverse() só funciona com listas.

Já a função reversed() funciona com qualquer iterável.

Sua função é inverter o iterável.

A função reversed() retorna um iterável chamado List reverse iterator

"""

# Exemplos

lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)
print(type(res))

# Podemos converter o elemento retornado para uma Lista, Tupla ou conjunto

# Lista
print(list(reversed(lista)))

# tupla
print(tuple(reversed(lista)))

# OBS: Em conjuntos, não definimos a ordem dos elementos
# conjunto (Set)
print(set(reversed(lista))) 

# Podemos iterar sobre o reversed
for letra in reversed('Geek University'):
    print(letra, end='')

print("\n")

# Podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed('Geek University'))))

# Podemos usar o slice de string para inverter uma string
print('Geek University'[::-1])

# Podemos também utilizar o reversed() para fazer um loop for reverso
for l in reversed(range(0, 10)):
    print(l)
    s
# Apesar quetambém já vimos como fazer isso utilizando o próprio range()
for l in range(9, -1, -1):
    print(l)