import math
from sqlite3.dbapi2 import sqlite_version
from string import printable

# math.prod - retorna o produto de um container númerico

num_v1 = [2, 3, 6, 7]
num_v2 = [2, 3, 6, 7]
num_v3 = [2, 3, 6, 7]

resultado = math.prod(num_v1)
resultado = math.prod(num_v2)
resultado = math.prod(num_v3)


# math.isqrt() - retorna a raiz quadrada inteira de um número

print(math.isqrt(9))  # retorna a raiz quadrada inteira de 9
print(math.sqrt(9))
print(math.isqrt(17))  # retorna a raiz quadrada inteira de 17
print(math.sqrt(17))


# math.dist() - retorna a distância euclidiana entre dois pontos


# pontos 3d
p3d1 = (12, 50, 40)
p3d2 = (6, 7, 13)


# pontos 2d
p2d1 = (12, 50, 40)
p2d2 = (6, 7, 13)


print(math.dist(p3d1, p3d2))
print(math.dist(p2d1, p2d2))


# math.hypot - retorna a hipotenusa de um triângulo retângulo
print(math.hypot(*p3d1))
print(math.hypot(*p2d1))


# Estatistica
#
# statistics.fmean - retorna a média aritmética de um container númerico
import statistics

valores_reais = [10.45, 15.65, 20.8, 25.1, 30.98]
valores_inteiro = [10, 15, 20, 25, 30]

print(statistics.fmean(valores_reais))
print(statistics.fmean(valores_inteiro))


# statistics.geometric_mean - retorna a média geométrica de um container númerico
#
print(statistics.geometric_mean(valores_reais))
print(statistics.geometric_mean(valores_inteiro))


# statistics.multimode - retorna o valor mais frequente de um container


seq1 = "geek university"
seq2 = [3, 5, 3, 8, 7, 9]
seq3 = [1, 2, 3, 1, 2, 3, 4, 5, 6]

print(statistics.multimode(seq1))
print(statistics.multimode(seq2))
print(statistics.multimode(seq3))
