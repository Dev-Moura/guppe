"""
Map

Com map, fazemos mapeamento de valores para função.
"""

import math

def area(r): 
  "Calcula a área de um círculo com raio 'r'."
  return math.pi * (r ** 2)

print(area(2))
print(area(5.3))


raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum
areas = []
for r in raios:
  areas.append((area(r)))

print(areas)

# forma 2 - map

# Map é uma função que recebe dois parâmetros: O primiero a função, o segundo um iterável

areas = map(area, raios)
print(areas)
print(type(areas))
print(list(areas))

# Forma 3 - com lambdas
print(list(map(lambda r: math.pi * (r ** 2), raios)))

# OBS: Após utilizar a função map() depois da primeira utilização do resultado, ele zera.
"""
Fixando - map

temos dados iteráveis.
dados: a1, a2..., an
temos uma função:
função: f(x)
utilizamos a função map(f, dados) onde map irá 'mapear' cada elemento dos dados e aplicar a função
O Map Object: f(a1), f(a2), f(...), f(an)
"""

# Exemplo

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los angeles', 26), ('Tokio', 27), ('Nova York', 28), ('Londres', 22)]

print(cidades)

# f = 9/5 * c + 32 

# Lambda

c_para_f = lambda dado:(dado[0], (9/5) * dado[1] + 32)

print(list(map(c_para_f, cidades)))
print(list(map(lambda dado:(dado[0], (9/5) * dado[1] + 32), cidades))) # Assim também está correto