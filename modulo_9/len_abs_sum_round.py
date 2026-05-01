"""
Len, abs, sum, round

# Len

len() -> retorna o tamanho (ou seja, o número de itens) de um iterável.

"""

# Só pra revisar

print(len('Geek University'))

print(len([1, 2, 3, 4, 5]))

print(len((1, 2, 3, 4, 5)))

print(len({1, 2, 3, 4, 5}))

print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))

print(len(range(0, 10)))

# Por debaixo dos panos, quando utilizamos a função len() o Python faz o seguinte:

# Dunder len
print('Geek University'.__len__())

# ABS

# abs() -> Retorna o valor absoluto de um número inteiro ou real. De forma básica, seria o seu valor real sem o sinal.

# Exemplo Abs

print(abs(-5))
print(abs(5))
print(abs(-3.14))
print(abs(3.14))

# sum

# sum() -> Recebe como parâmetro um iterável e retorna a soma dos seus itens. Podemos também informar um valor inicial, ou seja, um valor a ser somado com os itens do iterável.

#OBS: O valor inicial default é 0.

# Exemplos sum

print(sum([1, 2, 3, 4, 5]))

print(sum([1, 2, 3, 4, 5], 10))

print(sum([1, 2, 3, 4, 5], -10))

print(sum({1, 2, 3, 4, 5}, 10))

print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values))

# Round() -> Retorna um número arredondado para n dígitos de precisão após a vírgula decimal. Se n não for fornecido, ele arredonda para o inteiro mais próximo.

# Exemplos round

print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(10.5, 0))
print(round(10.5, 1))
print(round(1.2121212122121, 2))


