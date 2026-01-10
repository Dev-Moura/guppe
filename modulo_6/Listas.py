"""
Docstring for modulo_6.Listas

Listas

Listas em Python funcional como vetores/matrizes (arrays) em outras linguagens, como a diferença
de serem DINÂMICO e também de podermos colocar QUALQUER tipo dado.

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo:
    Ou seja, nestas linguagens se você criar um array do tipo int e com o tamanho 5, este array
    será sempre do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.


    
Já em Python:

- Dinâmico: Não possuem tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo; Ou seja, podemos colocar qualquer tipo de dado;

As listas em Python são representadas por colchetes: []
"""

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G','e','e','k',' ','U','n','i','v','e','r','s','i','t','y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

# Podemos facilmente checar se determinado valor está contido na lista

num = 18
if 18 in lista4:
    print(f"Encontrei o número {num}")
else:
    print("Não encontrado")

# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrências de uma valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementos em listas
# utilzamos a função append, com o append, nós só conseguimos add 1 elemento por vez
# lista1.append(12, 34, 56) = Error
print(lista1)
lista1.append(42)
print(lista1)

# uma lista dentro de outra lista
lista1.append([8, 3, 1]) # Coloca a lista como elemento único (sublista)
print(lista1)

if [8, 3, 1] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

# Jeito certo de add muitos itens numa lista 
lista1.extend([123,44,67])
print(lista1) 

# Podemos inserir um novo elemento na lista informando o índice
# OBS: Isso não substitui o valor inicial. O mesmo será deslocado para direita na lista.
lista1.insert(2, 'novo valor')
print(lista1)

# Podemos juntar duas listas
# lista1 = lista1 + lista2
# lista1.extend(lista2)
lista6 = lista1 + lista2
print(lista6)

# Invertendo a lista
# Forma 1
lista1.reverse()
lista2.reverse()
# Forma 2
lista1[::-1]
lista2[::-1]

# Copiando uma lista
lista6 = lista2.copy()
print(lista6)

# Podemos contar quantos elementos contém em uma lista
print(len(lista1))

# Podemos remover o ultimo elemento de uma lista
# O pop não somente remove o último elemento mas, também retorna
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo índice
# Os elementos á direta deste índice serão deslocados para a esquerda.
# Se não houver elemento no índice informado, teremos o erro IndexError.

lista5.pop(2)
print(lista5)

# Criando uma var de exemplo para remoção de lista
print(lista6)
lista7 = lista6.copy()
print(lista7)

# removendo todos os elementos
lista7.clear()
print(lista7)


# Podemos repetir elementos em uma lista
nova = [1, 2, 3]
nova = nova * 3
print(nova)

# Podemos converter uma string para uma lista
# Exemplo
curso = 'Programação em python: Essencial'
print(curso)
curso = curso.split()
print(curso)
# Por padrão, o split separa os elementos da lista pelo espaço entre elas

# Exemplo 2
curso2 = "Programação,em,python:,Essencial"
curso2 = curso2.split(",")
print(curso2)

# Convertendo uma lista em String
lista6 = ['Programação', 'em', 'python', 'essencial']
print(lista6)

# Abaixo estamos falando: Pega a lista6, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

# Abaixo estou falando: Pega a lista6, colcao cifrão entre cada elemento e transforma em uma string
curso = '$'.join(lista6)
print(curso)

# Podemos realmente colcoar qualquer tipo de dado em uma lista, inclusve misturar esses dados
lista6 = [1,2.34,True,'geek','d', [1,2,3] , 456465456]
print(lista6)
print(type(lista6))

# Iterando sobre listas

# Exemplo 1 - Utilizando for

soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 - Utilizando while

carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Utilizando variáveis em listas
numeros = [1,2,3,4,5]

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Fazemos acesso aos elementos de forma indexada

#           0         1         2       3
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0]) # verder
print(cores[1]) # amarelo
print(cores[2]) # azul
print(cores[3]) # brancos

# Fazemos acesso aos elementos de forma indexada inversa
# Para entender melhor o índice negativo. pense na lista como um círculo, onde
# o final de um elemento está ligado ao início da lista

print(cores[-1]) # branco
print(cores[-2]) # azul
print(cores[-3]) # amaralo
print(cores[-4]) # verde    


cores2 = ['laranja', 'vermelho', 'preto', 'cinza']

for cor in cores2:
    print(cor)

indice = 0 
while indice < len(cores2):
    print(cores2[indice])
    indice = indice + 1


# Gerar indice em um for
for indice, cor in enumerate(cores2):
    print(indice, cor)

# Listas aceitam valores repetidos
lista8 = []
lista8.append(42)
lista8.append(42)
lista8.append(33)
lista8.append(42)

print(lista8)


# Outros métodos não tão importantes mas também úteis

# Encontrar o índice de um elemento na lista

numeros = [5, 6, 7, 5, 8, 9, 10,]

# Em qual índice está o valor 6?
print(numeros.index(6))

# Em qual índice está o valor 9?
print(numeros.index(9))

# Caso não tenha este elemento na lista, será apresentado error ValueError

print(numeros.index(5)) # Retonar o índice do primeiro elemento encontrado

# Podemos fazer busca dentro de um range, ou seja, qual índice começar a buscar
print(numeros.index(5, 1))

# Podemos fazer busca de um range, inicio/fim
print(numeros.index(8,3,8)) # Busca o índice do valor 8, entre os índices 6 a 8


# Revisão de slicing

# lista[inicio:fim:passo]
# range[inicio:fim;passo]

# Trabalhando com slice de lista com o parâmetro 'ínicio'

lista =  [1,2, 3, 4,]

print(lista[1:]); # Iniciando no índice 1 e pegando todos os elementos restantes

# Trabalhando com slice de lista com parâmetro 'fim'

print(lista[:2]) # começa em 0, pega até o índice 2 - 1

print(lista[:4]) # Começa em 0, pega até o índice 4 - 1

print(lista[1:3]) # começa em 1, pega até o índice 3 - 1

# Trabalhando com slice de lista com o parâmetro 'passo'

print(lista[1::2]) # Começa em 1, vai até o final, de 2 em 2

print(lista[::2]) # Começa em 0, vai até o final, de 2 em 2

# Invertendo valores em uma lista

nomes = ['Geek', 'University']

nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

nomes.reverse()
print(nomes)

# soma, valor máximo, valor mínimo, tamanho

# * Se os valores forem todos inteiros ou reais.

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista)) # soma
print(max(lista)) # máximo valor
print(min(lista)) # máximo valor
print(len(lista)) # máximo valor

# Transformar uma lista em tupla

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desempacotamento de listas

# Se tiver mais elementos para desempacotar do que variáveis para receber os valores,
# teremos ValueError
lista = [1, 2 ,3]
num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)


# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Forma 1
# Veja que ao utilizamos lista.copy copiamos os dados da lista para nova lista, mas elas
# ficaram totalmente independentes, ou seja, modificando uma lista, não afeta a outra
# isso em python é chamado de deep copy
lista = [1, 2, 3]
print(lista)

nova = lista.copy()

print(nova)

nova.append(4)

print(lista)
print(nova)

# Forma 2 - Shallow copy
# Veja que foi utilizado a cópia via atribuição e copiamos os dados da lista para a nova lista mas,
# após realizar modificação em uma das listas, essa modificação se refletiu em ambas as listas
# isso em python é chamado de shallow copys
lista = [1, 2, 3]
print(lista)

nova = lista # cópia

print(nova)

nova.append(4)

print(lista)
print(nova)
