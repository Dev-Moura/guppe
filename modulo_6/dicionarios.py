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

# Adicionando elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

# Forma 1

receita['abr'] = 350

print(receita)

# Forma 2

novo_dado = {'mai': 500}

receita.update(novo_dado) # receita.update({'mai': 500})

print(receita)

# Atualizando dados em um dicionário

# Forma 1

receita['mai'] = 550

print(receita)

# Forma 2

receita.update({'mai': 600})
print(receita)

# CONCLUSÃO: A forma mais fácil e prática de adicionar ou atualizar dados em um dicionário é a mesma.
# CONCLUSÃO: Em dicionários, NÃO podemos ter chaves repetidas.

# Remover dados de um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

# Forma 1
# Aqui precisamos SEMPRE infromar a chave do item que queremos remover, caso não encontre o item, será gerado o erro KeyError
ret = receita.pop('mar')
print(ret)

# Ao removermos um objeto, o valor deste objeto é sempre retornado.
print(receita)

# Forma 2 

del receita['fev']

print(receita)

# KeyError se a chave não for encontrada
# Neste caso o valore removido não é retornado.
del receita['fev']

# Imagine que você tem um comércio eletrônico, onde temos um carrinho de compras na qual adicionamos produtos.
"""
Carrinho de compras
    produto 1:
        - nome;
        - quantidade;
        - preço;
    produto 2:
        - nome;
        - quantidade;
        - preço;
"""

# 1 - Poderiamos utilizar uma lista para isso? Sim

carrinho = []

produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teríamos que saber qual é o índice de cada informação no produto.

# 2 - Poderiamos utilizar uma tupla para isso? Sim

produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('God of War 4', 1, 150.00)

carrinho = (produto1, produto2)

print(carrinho)

# Teríamos que saber qual é o índice de cada informação no produto.

# 3 - Poderiamos utilizar um dicionário para isso? Sim

carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preço': 2300.00}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preço': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto, podemos ter a certeza
# sobre cada informação.

# Métodos de dicionários.

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# Limpar o dicionário (Zerar dados)

d.clear()
print(d)

# Copiando um dicionário para outro
# Forma 1 Deep Copy

novo = d.copy()  
print(novo)

novo['d'] = 4

print(d)
print(novo)

# Forma 2 Shallow Copy

novo = d

print(novo)

novo['d'] = 4

print(d)
print(novo)

# Forma não usual de criação de dicionários

outro = {}.fromkeys('a', 'b')  # Cria as chaves com o valor informado

print(outro)
print(type(outro)) 

usuario = {}.fromkeys(['nome', 'pontos', 'idade', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# O método fromkeys recebe dois parâmetros: um iterável e um valor.
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)
print(type(veja))

veja = {}.fromkeys(range(1, 11), 'novo')

print(veja)
