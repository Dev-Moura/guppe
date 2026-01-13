"""
Docstring for modulo_6.tuplas

Tuplas (tuple)

Tuplas são bastante parecidas com listas.

Existem basicamente duas diferenças básicas:

1 - As tuplas são representadas por parênteses ()

2 - As tuplas são imutáveis: Isso significa que ao se criar uma tupla ela não muda.
Toda operação em uma tupla gera uma nova tupla.


"""

print(type(()))

# CUIDADO 1 : As tuplas são representadas por parênteses, mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

# CUIDADO 2: Tuplas com 1 elemento

tupla3 = (4) # Isso não é tupla!
print(tupla3)

print(type(tupla3))

tupla4 = (4,) # Isso é uma tupla!
print(tupla4)

print(type(tupla4))

tupla5 = 4,
print(tupla5)

print(type(tupla5))


# CONCLUSÃO: Podemos concluir que tuplas são definidas pela virgula, e não
# pelo uso de parênteses
# (4) -> Não é tsupla
# (4,) -> É tupla
#  4, -> É tupla

tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tupla

tupla = ('Geek university', 'Programação em Python: Essencial')

escola, curso = tupla
print(escola)
print(curso)

# OBS: Gera erro (ValueError) se colocarmos um número diferente de elementos
# para desempacotar

# Métodos para Adição e remoção de elementos nas tuplas não exitem,
# tuplas são imutáveis

# soma*, Valor Máximo*, Valor Mínimo* e Tamanho
# * Se os valores forem todos inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6, 'b')

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas

tupla1 = (1,2,3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2) # tuplas são imutáveis

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2

print(tupla3)
print(tupla1)
print(tupla2)

tupla1 + tupla1 + tupla2 # tuplas são imutáveis, mas podemos sobrescrever seus valores
print(tupla1)

# Verificar se determinado elemento está contido na tupla

tupla = (1, 2, 3)

print(3 in tupla)


# Iterando sobre uma tupla

tupla = (1 ,2 ,3)

for i in tupla:
    print(i)


for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')

print(tupla.count('c'))

escola = tupla('Geek University')
print(escola.count('e'))

# Dicas na utilização de tuplas

# Devemos utilizar tuplas SEMPRE que não precisamos modifcar os dados contidos em uma coleção 

# Exemplo 1

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho')

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho')

meses.append('playstation')
print(meses)

# O acesso a elementos de uma tupla também é semelhante a de uma lista

print(meses[5])

# Iterar com while

i = 0

while i < len(meses):
    print(meses[i])
    i = i + 1

# Verificamos em qual índice um elemento está na tupla

print(meses.index('junho', 6))

# OBS: Caso o elemento não exista, será gerado ValueError
 
# Slicing

# tupla[inicio: fim: passo]

print(meses[5:9])

# Por quê utilizar tuplas?

# - Tuplas são mais rápidas do que listas.
# - Tuplas deixam seu código mais seguro.

# - Isso porque trabalhar com elementos imutáveis traz segurança para o código

# Copiando uma tupla para outra

tupla = (1, 2, 3)
print(tupla)

nova = tupla # Na tupla não temos o problema de Shallow Copy

print(nova)
print(tupla)

outra = (4, 5, 6)

nova = nova + outra

print(nova)
print(tupla)


