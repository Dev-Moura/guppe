"""
List Comprehension - Parte 1

- Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de outro iterável.

# Sintaxe da List Comprehension
[dado for dado in iterável]
"""

# Exemplo

numeros = [1, 2, 3, 4, 5]

naruto = [numero * 10 for numero in numeros]
print(naruto)

numeros2 =  [numero / 2 for numero in numeros]
print(numeros2)

def funcao(valor):
    return valor * valor

numeros = [funcao(numero) for numero in numeros]
print(numeros)

# List Comprehension versos Loop

# Loop python básico
numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []

for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados)


# List Comprehension python avançado
print([numero * 2 for numero in numeros])

# Outros Exemplos
# 1

nome = 'Geek University'

print([letra.upper() for letra in nome])

# 2
def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

amigos = ['maria', 'jilia', 'pedro', 'guilherme', 'vanessa']

print([caixa_alta(amigo) for amigo in amigos])

# 3
print([numero * 3 for numero in range(1, 10)])

# 4 
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# 5
print([str(numero) for numero in [1, 2, 3, 4, 5]])