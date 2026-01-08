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
# OBS: Os elementos á direta 
lista5.pop(2)
print(lista5)

