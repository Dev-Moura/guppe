"""
Reduce

OBS: A partir do Python3+ a função reduce() não é mais um função integrada (built-in). Agora temos
que importar e utilizar esta função a partir do módulo 'functools'.

Guido Van Rossum: Utilize a função reduce() se você realmente precisa dela. Em todo caso,
99% das vezes, um loop for é mais legível.

Para entender o reduce() 

# Imagine que temos uma coleção de dados:

dados - [a1, a2, a3, a4, a5, ... an]

# E temos uma função que recebe dois parâmetros:

def funcao(x, y):
    return x * y

Assim como map() e filter(), a função reduce() recebe dois parâmetros, sendo uma função e um iterável.

reduce(funcao, dados)

A função reduce(), funciona da seguinte forma:
    passo 1: res1 = f(a1, a2) # Aplica a função nos dois primeiros elementos de coleção e guarda o resultado e guarda o e resultado.
    passo 2: res2 = f(res1, a3) # Aplica a função passando o resultado do passo1 mais o terceiro elemento e guarda o res

    e isso é repetido até o final da coleção, ou seja, até o an. O resultado final é o resultado da aplicação da função para toda a coleção de dados.
    Passo 3: res3 = f(res2, a4)
    .
    .
    .
    passo n: resn = f(resm, an)

ou seja, em cada passo ele aplica a função passando como primeiro argumento o resultado da aplicação anterior. No final,
reduce() irá retornar o resultado final.

Alternativamente, podemos pensar que a função reduce() pega os dois primeiros elementos da coleção e aplica a função, depois pega o resultado e o próximo elemento da coleção e aplica a função novamente, e isso é repetido até o final da coleção.

funcao(funcao(funcao(a1), a2), a3), a4), ...), an)
"""

# Como funcioan na prática?

# Vamos utilizar a função reduce() para multiplicar todos os números de uma lista

from functools import reduce

dados = [2, 3, 4, 5, 6, 7, 8, 9, 10]

# Para utilizar o reduce() nós precisamos de uma função que receba dois parâmetros, ou seja, a função deve ser binária.
multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)

# Utilizando o loop normal

res = 1 

for n in dados:
    res = res * n

print(res)

