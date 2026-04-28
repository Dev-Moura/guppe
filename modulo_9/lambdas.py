"""
Uitlizando Lambdas

Conhecidas por expressoes lambdas funcao sem nome igual arrow function do js
"""

# função em python

def funcao(x):
    return 3 * x + 1

print(funcao(4))
print(funcao(7))

# Expressão Lambda

lambda x: 3 * x + 1

# E como utilizar a expressão?
# Não pythonico
calc = lambda x: 3 * x + 1 

print(calc(4))
print(calc(7))

# Podemos ter expressões lambdas com múltiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo(' angelina', 'JOLIE'))
print(nome_completo(' FELICITY    ', ' JONES  '))

# Em funções python podemos ter nenhum ou várias entradas. Em lambdas também

amar = lambda: 'como não amar python? '

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y ,z:  3 / (1 / x + 1 / y + 1 / z)

# n = lambda x1, x1, ..., xn: <expressão>

print(amar)
print(uma)
print(duas)
print(tres)

# OBS: se passar argumentos demais vai dar typeError

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card', 'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']


print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)

# func quadrática
# f(x) = a * x ** 2 + b * x + c

# Definindo a função

def geradora_funcao_quadratica(a, b, c):
    """ Retorna a função x """
    return lambda x: a * x ** 2 + b * x + c

reste = geradora_funcao_quadratica(2, 3 , -5)

print(teste(0))
print(teste(1))
print(teste(2))

