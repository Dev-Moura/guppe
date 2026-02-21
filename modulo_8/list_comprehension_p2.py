"""
List Comprehension

Nós podemos adicioanr estruturas condicionais lógicas Às nossas List comprehension
"""

# Exemplo

numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]

impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares) 

# refatorando

# Qualquer número que for par módulo de 2 é 0 e 0 em python é false. not False = True
pares = [numero for numero in numeros if not numero % 2]

# Qualquer número impar módulo de 2 é 1, e 1 em Python é True
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)  

# 2

res = [numero * 2 if numero % 2 == 0 else numero /2 for numero in numeros]
print(res)