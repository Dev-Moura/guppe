"""
Módulo Collection - nNamed Tuple


# Recap tupla
tupla = (1, 2, 3)

print(tupla[1])

Named Tupla -> São tupla, diferenciadas, onde, especificamos um nome para a mesma e também parâmetros.
"""

# Importando

from collections import namedtuple

# Precisamos definir o nome e parâmetros.

# Forma 1

cachorro1 = namedtuple('cachorro', 'idade raca nome')

# Forma 2

cachorro2 = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3

cachorro3 = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando

ray = cachorro1(idade=2, raca='chow-chow', nome='Ray')
print(ray)

# Acessando os dados

# Forma 1 - via indexação

print(ray[0]) # Idade
print(ray[1]) # Raça
print(ray[2]) # Nome

# Forma 2 - via variável

print(ray.idade) # idade
print(ray.raca) # idade
print(ray.nome) # idade

print(ray.index('Chow-Chow'))

print(ray.count('Chow-Chow'))