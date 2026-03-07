"""
Set Comprehesion

lista = [1, 2, 3, 4, 5]
set = {1, 2, 3, 4, 5}

"""

# Exemplos

num = {num for num in range(1, 7)}
print(num)

# other Exemplo

numbers = {x ** 2 for x in range(10)}
print(numbers)


numbers = {x: x ** 2 for x in range(10)}
print(numbers)

# to finish 

words = {word for word in 'Geek University' }