"""
Docstring for modulo_7.funcoes_com_parametro

- Funções que recebem dados para semre processados dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:

entrada -> processamento -> saída

Se a gente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída;

"""

# Refatorando uma função

def quadrado(numero):
    # return numero * numero
    return numero ** 2

print(quadrado(10))


def cantar_parabens(aniversariante):
    print('Parabens! pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('muitos anos de vida')
    print(f'Viva o/a {aniversariante}!')

cantar_parabens('Maria')

# Funções podem ter n parâmetros de entrada. Ou seja, podemos receber como entrada
# em uma função quantos parâmetros forem necessários. Eles são separados por vírgula.

# Exemplos

def soma(a, b):
    return a + b

def multiplica(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 + b) * msg

print(soma(5, 7))
print(soma(10, 20))

print(multiplica(4, 5))
print(multiplica(2, 8))

print(outra(3, 2, 'Ola '))  # Vai repetir
print(outra(5, 4, 'Python'))      # Vai multiplicar

print(multiplica(50, "="))

# OBS: Se a gente informar um número diferente de argumentos, teremos um TypeError
# print(soma(5))  # TypeError
# print(soma(5, 6, 7))  # TypeError  

# Nomeando parâmetros

def nomecompleto(nome, sobrenome): # isso é parâmetro
    return f'Seu nome completo é {nome} {sobrenome}' 

print(nomecompleto('Angelina', 'Jolie')) # isso é argumento

# A diferença entre parâmetros e argumentos

# PAraêtros são as variáveis declaradas na definição de uma função;
# Argumentos são os valores passados durante a execução de uma função;

nome = 'Felicity'
sobrenome = 'Jones'

# A ordem importa
print(nomecompleto(sobrenome, nome)) # Aqui os argumentos foram passados na ordem inversa

# Argumentos nomeados (Keyword Arguments)
print(nomecompleto(nome='Angelina', sobrenome='Jolie'))
print(nomecompleto(nome=nome, sobrenome=sobrenome))
print(nomecompleto(sobrenome='Marques', nome='Marcia'))


# Erro comum na utilização do return

def soma_impares(numeros):
    total = 0
    for numero in numeros:
        if numero % 2 != 0:
            total += numero
#            return total  # ERRO: O return está dentro do for, fazendo a função retornar na primeira iteração
    return total

lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))

tupla = 1, 2, 3, 4, 5, 6, 7
print(soma_impares(tupla))