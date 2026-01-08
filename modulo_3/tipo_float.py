"""
Tipo float

tipo real, decimal

casas decimais

OBS: O separador de casas decimais na programação é o ponto e não a vírgula.

# Errado
valor_1 = 1, 44
print(valor_1)
print(type(valor_1))

# Certo
valor = 1.44
print(valor)
print(type(valor))

# dupla atribuição é permitido igual em java
valor1, valor2 = 1, 55
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

"""
#  Podemos converter um float para um int
# OBS: Ao converter valores float para inteiros nos perdemos precisão igual em java

valor = 1.44

res = int(valor)
print(res)
print(type(res))

#  Podemos trabalhar com numeros complexos

variavel = 5j
