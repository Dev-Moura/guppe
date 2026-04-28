"""
Generators 

Em aulas anteriores nós estudamos:
- List Comprehension
- dict Comprehension
- set Comprehension

Não vimos: 
- Tuple Comprehension... por que elas se chamam generators e não tuple comprehension?

nomes = ['Carlos', Camila', 'Carla', 'Cristina', 'Vanessa']

print(any(nome[0] == 'C' for nome in nomes))

nomes = ['Carlos', 'Camila', 'Carla', 'Cristina', 'Vanessa']

print(any(nome[0] == 'C' for nome in nomes))

#List Comprehension

res = [nome[0] == 'C' for nome in nomes]
print(type(res))

# Generator Expression
res = (nome[0] == 'C' for nome in nomes)
print(type(res))

# Retorna a quantidadede bytes em memória do elemento passado como parâmetro
from sys import getsizeof

# Mostra quantos bytes a string 'Geek' está ocupando em memória. Quanto maior a string, mas espaço ocupa.
print(getsizeof('Geek'))




"""

from sys import getsizeof

# gerando uma lista de números com list comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# gerando uma lista de números com Set comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# gerando uma lista de números com Dict comprehension
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números com o generator
gen_comp = getsizeof(x * 10 for x in range(1000))

print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dict Comprehension: {dict_comp} bytes')
print(f'Generator Expression: {gen_comp} bytes')
