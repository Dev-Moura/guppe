"""
Docstring for modulo_6.entendendo_explorando_range

Ranges

- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequências númericas, não de forma aleatória
mas sim de maneira especificada.


Formas gerais:

range(valor_de_parada)

OBS: VALOR DE PARADA NÃO INCLUSIVE (início padrão 0, e passo de 1 em 1)


"""

# Forma 1
for num in range(11):
    print(num)


# Forma 2 valor_de_início + valor_de_parada
# range(valor_de_parada não inclusive (início especificado pelo usuário, e passo de 1 em 1))
for num2 in range(1, 11):
    print(num2)

# Forma 3 
# range (valor_de_início, valor_de_parada, passo)

for num3 in range(1, 10, 2):
    print(num3)

# Forma 4 (inversa)
# range (valor_início, valor_de_parada, passo)

for num4 in range(10, 0, -1):
    print(num4)
