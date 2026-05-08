"""
Random

- Em python, módulos nada mais são do que outros arquivos python.

modulo random ->  possui várias funções para geração de números pseudo-aleatório.


"""
# OBS: existem duas formas de se utilizar um módulo ou função deste

# forma 1 - importando todo o módulo (Não recomendado).

import random

# Ao realizar o import de todo o módulo, todas as funções,a tributos, classes e propriedades que estiverem
# dentro do módulo ficarão disponíveis(ficarão em memória). Caso você saiba exatamente as funções que você
# precisa deste módulo, então esta não seria a forma ideal de utilizar.

print(random.random())

# Utilizamos a função random() do módulo random para gerar um número pseudo-aleatório entre 0 e 1.
# nos colocamos o nome do pacote seguido de um ponto e o nome da função, separado por um ponto.
 
# Forma 2 - importando uma função específica do módulo

from random import random

# no import acima, estamos importando apenas a função random() do módulo random. Desta forma, apenas esta função

print(random())


for i in range(10):
    print(random())

# uniform() -> Gera um número real pseudo-aleatório entre os valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(3, 7)) # Gera um número entre 3 e 7
    # veja que o número 7 não é incluído, ou seja, o intervalo é fechado em 3 e aberto em 7.


# randint() -> Gera um número inteiro pseudo-aleatório entre os valores estabelecidos
from random import randint

for i in range(6):
    print(randint(1, 61), end=', ' ) # comeca de 1 evai até 60


# choice() -> Mostra um valor aleatório entre um iterável

jogadas = ['pedra', 'papel', 'tesoura']

from random import choice

print(choice(jogadas))


# shuffle() -> Embaralha os dados de um iterável

from random import shuffle

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10']

print(cartas)

shuffle(cartas)

print(cartas.pop()) # Mostra a última carta do baralho