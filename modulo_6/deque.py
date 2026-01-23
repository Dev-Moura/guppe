"""
Docstring for modulo_6.deque

Módulo Colletion - Deque

Podemos dizer que o deque é uma lista de alta performance.
"""

# Importa

from collections import deque

# Criando deques

deq = deque('geek')
print(deq)

# Adicionando elementos no deque

deq.append('y') # Adiciona no final
print(deq)

deq.appendleft('k') # Adiciona no começo
print(deq)

# Remover um elemento

print(deq.pop()) # Remove e retornar o último elemento
print(deq)

print(deq.popleft()) # Remove e retornar o primeiro elemento
print(deq)