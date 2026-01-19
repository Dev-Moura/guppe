"""
Docstring for modulo_6.conjuntos

Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência à Teoria dos conjuntos da mátematica.

- Aqui no Python, os conjuntos são chamados de Sets.

Dito isto, da mesma forma que na matemática:

- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos
mas não nos importamos com a ordenação deles. quando não precisamos se preocupar
com chaves, valores e itens duplicados.

Os conjuntos (sets) são referênciados em Python com chaves {}

Diferença entre conjuntos (Set) e Mapas (Dicionários) em Python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;

"""

# Definindo um conjunto:

# Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) # Repare que temos valores repetidos.

print(s)
print(type(s))

# OBS: Ao criar um conjunto , caso seja adicionado um valor já existente, o mesmo
# será ignorado sem gerar erro e não fará parte do conjunto.

# Forma 2 - mais comum

s = {1, 2, 3, 4, 5,}
print(s)
print(type(s))

# Podemos verificar se determinado elemnto está contido no conjunto

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')


# Importante lembrar que, além de não termos valores duplicados, não temos ordem

# Lista aceitam valores, duplicados, então temos 10 elmentos
lista = [99, 2, 34, 23, 12, 1, 44, 5, 2, 34]
print(f'Lista: {lista} com {len(list)} elementos')

# Tuplas aceitam valores duplicados, então temos 10 elementos
tupla = 99, 2, 34, 23, 12, 1, 44, 5, 2, 34
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# Dicionario não aceitam chaves duplicadas, então temos 8 elementos
dicionario = {}.fromkeys([99, 2, 34, 23, 12, 1, 44, 5, 2, 34], 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')

# Conjunto não aceitam valores duplicados, então temos 8 elementos
conjunto = {99, 2, 34, 23, 12, 1, 44 , 5, 34}
print(f'Conjunto: {conjunto}')

# Assim como todo outro conjunto Python podemos colocar tipos de dados misturados em Sets
s = {1, 'b', True, 34.33, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente
for valor in s:
    print(valor)

# Usos interessantes com Sets

# Imagine que fizemos um form de cadastro de visitantes em uma feira ou museu e os visitantes
# Informam manualmente a cidade de onde vieram.

# Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novo elementos
# e ter repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']

print(cidades)
print(len(cidades))


# Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos.

# Podemos utilizar o set para isso

print(len(set(cidades)))

# Adcionando elementos em um conjunto

s = {1, 2, 3}

# Conjuntos são mutáveis
s.add(4)
s.add(4) # duplicidade não gera erro, simplesmente ignorado e não adiciona
print(s)

# Removendo elementos em um conjunto

# Forma 1

s.remove(3) # Não é índice! Informamos o valor a ser removido.
# s.remove(33)  # Aqui da erro, pois o valor não existe no conjunton gerando KeyError

print(s)

# Forma 2 

s.discard(2)
# s.discard(2) # Não exite no conjunto, não faz nada, pois não existe esse valor no conjunto


print(s)

# Conpiando um conjunto para outro...
conjuntos = {1, 2, 3 , 4}
print(conjuntos)


# Forma 1 - Deep Copy

novo = conjuntos.copy()
print(novo)

novo.add(5)

print(novo)
print(conjuntos)

# Forma 2 - Shallow Copy

novo = conjuntos

novo.add(6)
print(novo)
print(conjuntos)

# Podemos remover todos os itens de um conjunto

conjuntos.clear()
print(conjuntos)


# Métodos Matemáticos de conjuntos

# Imagine que temos dois conjunto:  Um contendo estudantes do curso Python e um
# contendo estudantes do curso de Java.

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Veja que alguns alunos que estudam Python também estudam Java.

# Precisamos gerar um conjunto com noems de estudantes únicos

# Forma - 1 - Utilizando union

# Não faz diferença a troca das variáveis aqui, pois vai fazer a junção desse conjunto.
unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# forma 2 - Uilizando o caractere pipe |
unicos2 = estudantes_java | estudantes_python

print(unicos2)

# Gerando um conjunto de estudantes que estão em ambos os cursos

# Forma 1 - Uilizando intersection

ambos1 = estudantes_python.intersection(estudantes_python)
print(ambos1)
# Forma 2 - Utilizando o &

ambos2 = estudantes_java & estudantes_python
print(ambos2)

# Gerando um conjunto de estudantes que não estão no outro curso

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho

# * Se os valores forem todos inteiros ou reaia

s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))
