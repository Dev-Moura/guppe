"""
Teste de Velocidade com Expressoes geradoras

"""

# Generators

def nums():
    for num in range(1, 10):
        yield num

ge1 = nums()

print(ge1)

print(next(ge1))
print(next(ge1))


ge2 = (num for num in range(1, 10))

print(ge2)

print(next(ge2))
print(next(ge2))

print(sum(num for num in range(1,10)))

# Realizando teste de velocidade
import time

# Generator expression

gen_inicio = time.time()
print(sum(num for num in range(1000000000)))
gen_tempo = time.time() - gen_inicio


# list comprehension

list_inicio = time.time()
print(sum([num for num in range(1000000000)]))
list_tempo = time.time() - list_inicio

print(f'Generator Expression levou {gen_tempo}')
print(f'List Comprehension levou {list_tempo}')


