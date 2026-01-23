"""
Módulo Collection: Orderend Dict
"""
# Em um dicionário a ordem de inserçõa dos elementos não é garantida
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for chave, valor in dicionario.items():
    print(f' Chave={chave}: valor={valor}')

# É um dicionario, que nos garante a ordem de inserção dos elementos
# Fazendo import
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'cahve={chave}:valor={valor}')

# Entendendo a diferença entre Dict e Ordered Dict

# Dicionario comuns

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2) # True, já que a ordem dos elementos não importa para o dicionário

# Ordered Dict
odict1 = OrderedDict({'a': 1, 'b':2 })
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2) # False, pois a ordem aqui difere, e a ordem importa para o OrderDict

