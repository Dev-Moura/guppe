"""
Docstring for modulo_6.mapas

Mapas -> Conhecidos em Pyhon como Dicionários

Dicionários em Python são representados por chaves {}
"""

receita = {'jan': 100, 'fev': 250, 'mar': 400}

# Iterar sobre dicionários

# Printando chaves

for chave in receita:
    print(chave)

# Pritando Valores

for chave in receita:
    print(receita[chave])

# Printando chave e valores

for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')

# Acessando as chaves

print(receita.keys())

for chave in receita.keys():
    print(receita[chave])


# Acessando os valores
print(receita.values())

for valor in receita.values():
    print(valor)

# Desempacotamento de dcionários

for chave, valor in receita.items():
    print(f' chave={chave} e valor={valor}')

# Soma*, valor Máximo*, valor Mínimo*, Tamanho

# * Se os valores forem todos inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita.values()))
