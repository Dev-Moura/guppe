"""
Teste de Memoria com Generators

# Sequencia de fibonacci
1, 1, 2, 3, 5, 8, 13, 21, 34

"""
import sys

# Funçao usando lista 449mb de recursos da maquina

"""
def fib_lista(max):
    nums = []
    a, b, = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums


for n in fib_lista(10000):
    print(n)
"""

# Fun usando geradores

def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador += 1

# teste
sys.set_int_max_str_digits(0)
for n in fib_gen(100000):
    print(n)