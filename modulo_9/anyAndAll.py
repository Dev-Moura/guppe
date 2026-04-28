"""
Any e All

all() -> retorna true se todos os elementos do iterável são verdadeiros ou ainda seo iterável está vazio.

# Exemplo all()

print(all([0, 1, 2, 3, 4])) # False

print(all([1, 2, 3, 4])) # True

print(all([])) # True
s
print(all([1, 2, 3, 4])) # True

print(all([1, 2, 3, 4])) # True

print(all('Geek')) # True

nomes = ['Carlos', 'Camila', 'Carla', 'Cristina', 'Vanessa']

print(all([nome[0] == 'C' for nome in nomes]))

# Um iterável vazio convertido em boolean é false, mas o all() entende com true
print(all([letra for letra in 'eio' if letra in 'aeiou']))

"""

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))


