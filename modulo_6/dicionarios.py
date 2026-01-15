"""
Docstring for modulo_6.dicionarios

Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos
por mapa.

Dicionários são coleções do tipo chave:valor


Dícionários são representados por chaves {}.

print(type{})

OBS: Sobre dicionários
    - Chave e valor são separados por dois pontos 'chave:valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dados;
    - Podemos misturar tipos de dados;
"""

# Criação de dicionários

# Forma 1 (Mais comum)

paises = {'br': 'Brasil', 'eua':'Estados Unidos', 'py': 'Paraguia'}

print(paises)
print(type(paises))

# Forma 2 (Menos comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')

print(paises)
print(type(paises))

# Acessando elementos 

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla

print(paises['br'])
print(paises['py'])
# print(paises['ru']) Caso tentamos fazer aum acesso utilizando uma chave que não existe, teremos o erro keyError

# Forma 2 - Acessando via get - recomendado

print(paises.get('br'))
# print(paises.get('ru')) Aqui ele não da erro, mas retorna um None

# Caso o get não econtreo o objeto com a chave informada será retornado o valor None e não será gerado KeyError

# pais = paises.get('ru)
# if pais:
#       print(f'Encontrei o pais {país}')
# else:
#       print(f'Não econtrei o país')

# Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada

pais = paises.get('ru', 'Não econtrado')
print(f'Encontrei o páis {pais}')

# Podemos verficar se determinada chave se encontra em um dicionário
print('br' in paises)
print('ru' in paises)
print('Estados unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

# Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla dicionários, como chaves
# de dicionários

# Tuplas por exemplo são bastante interessante de serem utilizadas como chaves de dicionários, pois as mesmas
# são imutáveis

localidades = {
    (35.6895, 39.6927): 'Escritório em Tókio',
    (40.7128, 74.0060): 'Escritório em Nova York',
    (37.7749, 122.4194): 'Escritório em Rio de Janeiro',
}

print(localidades)
print(type(localidades))