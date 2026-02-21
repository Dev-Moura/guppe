"""
Docstring for modulo_7.funcao_com_retorno

"""

numeros = [1, 2, 3]

ret_pop = numeros.pop()
print(f'Retorno de pop: {ret_pop}')

ret_pr = print(numeros)

print(f'Retorno de print: {ret_pr}')
 
# Exemplo funçao
def quadradado_de_7():
    print(7*7)

ret = quadradado_de_7()

print(f'retorno {ret}')

# Quando uma função não retornar nenhum valor, o retorno é none

# Vamos refatorar esta função para que ela retorne o valor

# Funções Python que retornam valores, devem retornar estes valores com a palavra resservada return
def quadradado_de_7():
    return 7 * 7

ret = quadradado_de_7()
print(f'Retorno {ret}')

# Não precisamos necessariamente criar uma variável para receber o retorno de uma função.
# Podemos passar a execução da função para outras funções.


# Criamos uma variável para receber o retorno da função
ret = quadradado_de_7()
print(f'Retorno {ret}')

print(f'Retorno: {quadradado_de_7()}')

# refatorando a primeira função

def diz_oi():
    return 'oi!'

diz_oi()