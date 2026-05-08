"""
Trabalhondo com modulos built-in do Python

"""
import random as rdm

print(rdm.random())  # Gerar um número aleatório entre 0 e 1

# Podemos importar todas as funções de um módulo usando o *
from random import *

print(random())

# importando todo o módulo
import random
print(random.random())

from random import randint as rdi
print(rdi(5, 89))  # Gerar um número inteiro aleatório entre 1 e 10

# Utilizando alias (apelidos) para módulos e funções

from random import randint as rdi, random as rdm
print(rdi(1, 10))  # Gerar um número inteiro aleatório entre 1 e 10
print(rdm())  # Gerar um número aleatório entre 0 e 1


# constumamos a utilizar o tuple para importar várias funções de um módulo
from random import (
    random,
    randint,
    shuffle, choice
)

print(random())  # Gerar um número aleatório entre 0 e 1
print(randint(1, 10))  # Gerar um número inteiro aleatório entre
print(choice(['Python', 'Java', 'C++', 'JavaScript']))  # Escolher um elemento aleatório de uma lista
lista = [1, 2, 3, 4, 5]
shuffle(lista)  # Embaralhar a lista
print(lista)