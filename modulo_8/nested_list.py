"""
Listas aninhadas

- Algumas linguagens de programação (C/Java) possuem uma estrutura de dados chamadas de arrays:
    - Unidimensionais (Arrays/Vetores);
    - Multidimensionais (Matrizes);

Em Python nós temos as listas

numeros =  [1, 'b', 3.234, True, 5]
"""

# Exemplos

lista = [[1,2,3], [4,5,6], [7,8,9]] # Matriz 3 x 3

print(lista)

print(type(lista))

# Como fazemos para acessar os dados?

print(lista[0][1]) # 2
print(lista[2][1]) # 2


# Iterando com loops em uma lista aninhada

# for lista in lista:
#     for num in lista:
#         print(num)

# List comprehesion

[[print(valor) for valor in lista ] for lista in lista]

# Outro exemplos

# Gerando um tabuleiro/matrix 3x3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else '0' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valores inicias

print([['*' for i in range (1, 4)] for j in range(1, 4)])