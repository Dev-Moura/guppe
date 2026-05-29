"""
Funçoes de maior grandeza - Higher Order Functions - HOF

Oque isso significa?

- Quando uma linguagem de programaçao suporta HOF, indica que podemos ter funçoes
que retornar outras funçoes como resultado ou memso que podemos passar funçoes
caso argumentos para outras funçoes , e ate mesmo criar uvariaveis do tpo de funçoes

OBS: Na seçao de funçoes, nos utilizamos isso.

Em Pyhotn, as funçao sao cidadoes de primeira classe
"""
from random import random


def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcular(num1, num2, funcao):
    return funcao(num1, num2)


print(calcular(4,3, somar))

print(calcular(4,3, diminuir))

print(calcular(4,3, multiplicar))

print(calcular(4,3, dividir))

# Nested Functions - Funçoes Aninhadas

# Em python podemos tambem ter funçoes, que sa conhecidas por nested functions
# ou tambem inner functions (funçoes Internas).

# Exemplo

from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(("E ai ", "Suma daqui ", "Gosto muito de voce "))
    return humor() + pessoa

print(cumprimento('Angelina'))

print(cumprimento("Felicity"))

print(cumprimento("Michael"))

# RETORNANDO A FUNÇAO de outras funçoes

def faz_me_rir():
    def rir():
        return choice(("hahahahahahah", "kkkkkkkkkkkk", "yayayayyayayayayay"))
    return rir #aqui nao retornar nada

rindo = faz_me_rir()

print(rindo()) # aqui a a var e adicionada o () que esta se referindo a funçao rir, logo rindo() retorna a funçao

# Nested function podem acessar o escopo de funçoes mais externas

from random import choice

def faz_me_novamente(pessoa):
    def dando_risada():
        risada = choice(("hahahahahahah", "lolololololololo", "kkkkkkkkkkkkkkkkk"))
        return f'{risada}! {pessoa}'
    return dando_risada

rindo = faz_me_novamente('Fernanda')
print(rindo())
print(rindo())
print(rindo())
