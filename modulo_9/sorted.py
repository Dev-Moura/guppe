"""
Sorted 

Obs: Não confunda, apesar do nome, com a função sort() que já estudamos em lsitas. O sort()
só funciona com listas.

podemos tuilizar o sorted() com qualquer iterável

ccomo o prórpio nome diz, sorted() serve para ordenar.
"""
# exemplo

numeros = [6, 1, 8, 2]
print(numeros)

print(sorted(numeros)) # Ordena do menor para o maior

print(numeros)


numeros = [6, 1, 8, 2]
print(numeros)


print(sorted(numeros))
# Adicionando parâmetros ao sorted()


print(sorted(numeros, reverse=True)) # Ordena do maior para o menor

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo Gatos"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

print(usuarios)

# Ordena por username - ORdem Alfabética
print(sorted(usuarios, key=lambda u: u["username"]))

print("\n")

# Ordenando pelo número de tweets
print(sorted(usuarios, key=lambda u: u["tweets"][0].lower() if u["tweets"] else ""))

# Último exemplo

musicas = [
    {"titulo": "Thunderstruck", "tocou": 1},
    {"titulo": "Dead Sking Mask", "tocou": 2},
    {"titulo": "Back in black", "tocou": 4},
    {"titulo": "Too old to rock'in'roll, to young to die", "tocou": 32},
]

# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda m: m['tocou']))

# Ordema da ,aos tocada para a menos tocada
print(sorted(musicas, key=lambda m: m['tocou'], reverse=True))
