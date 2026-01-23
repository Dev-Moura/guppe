"""
Docstring for modulo_6.exercicio_modulo_6
"""
# 1 exercicio

lista1: list[int] = []

while len(lista1) < 6:
    valor: int = int(input(f"informa o valor {len(lista1) + 1}/6: "))
    lista1.append(valor)

for valor in lista1:
    print(valor)

# 2 exercicio

A: list[int] = [1, 0, 5, -2, -5, 7]

soma: int = A[0] + A[1] + A[5]
print(soma)

A[5] = 100
print(A)

for valor in A:
    print(valor)

# 3 exercicio

listas: list[int] = []
count_pairs: int = 0

while len(listas) < 10:
    value: int = int(input(f"informa o valor {len(listas) + 1}/10: "))
    listas.append(value)

    if value % 2 == 0:
        count_pairs = count_pairs + 1

if count_pairs > 0:
    print(f' A lista {listas} possui {count_pairs} pares.')
else:
    print(f'A lista {listas} não possui valores pares.')