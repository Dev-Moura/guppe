"""
Docstring for modulo_6.break

Saindo de loops com break

Funciona da mesma forma que nas linguagens C ou Java.

Utilizamos o break para sair de loops de maneira projetada.

"""

# Exemplo 1

for num in range(0, 10):
    if num == 6:
        break
    else:
        print(num)
print('Sai do loop')

# Exemplo 2

while True:
    comando = input("Digite 'sair' para sair: ")
    if comando == 'sair':
        break