"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção

import statistics

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()

media = statistics.mean(dados)

print(f"Média: {media}")

# Assim como a função map(), a filter() recebe dois parâmetros, sendo

# uma função e um iterável.

res = filter(lambda x: x > media, dados)

print(list(res)) # depois de consumir o iterável, ele é esgotado, ou seja, não tem mais dados para serem filtrados

print(f'Novamente: {list(res)}')

# Assim como a função map(), a filter() retorna um iterável do tipo filter, ou seja, um generator, e para obter os dados filtrados, precisamos converter o resultado para uma coleção, como por exemplo, uma lista.

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', 'Equador', '', 'Venezuela']

print(paises)

# res = filter(lambda pais: len(paises) > 0, paises)

# res = filter(lambda pais: pais != '', paises)

res = filter(None, paises)

print(list(res))

# A diferença entre map() e filter() é:

# map() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função para cada elemento do iterável.

# filter() -> recebe dois parâmetros, uma função e um iterável e retornar um objeto filtrando apenas os elementos de acordo com a função. A função deve retornar True ou False para cada elemento do iterável.  

"""


usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo Gatos"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

# Filtrar os usuários que estão inativos no Twitter, ou seja, aqueles que não postaram nenhum tweet.

# Forma 1
inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))
print(inativos)

# Forma 2
inativos = list(filter(lambda u: not u['tweets'], usuarios))
print(inativos)

# Combinar filter() e map()

nomes = [
    'Vanessa',
    'Ana',
    'Maria'
]


# Devemos criar um lista contendo 'Sua instrutura é' + nome, desde que cada nome tenha 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)

