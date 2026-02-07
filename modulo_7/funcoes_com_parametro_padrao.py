"""
Docstring for modulo_7.funcoes_com_parametro_padrao

Funções com Parâmetro Padrao (Deafault Paramters)

- Funções onde a passagem de parâmetro seja opcional:

# Exemplo de função onde a passagem de parâmetro seja opcional
print('Geek University')

print()

# Exemplo de função onde a passagem de parâmetro seja obrigatória
def quadrado(numero):
    return numero ** 2

print(quadrado(3))
print(quadrado()) # TypeError

"""


def exponecial(num=4, poten=2):
    return num ** poten

print(exponecial(2, 3))
print(exponecial(3, 2))

print(exponecial(3))
print(exponecial(3, 5))

# OBS -> Se o usuário passar somente 1 parâmetro, este será atribuído ao parâmetro numero, e será calculado o quadrado deste número:
# Se o usuário passar 2 argumentos, o primeiro será atribuído ao parâmetro numero e o segundo ao parâmetro potencia. Então
# será calculada esta potência.

print(exponecial())

# OBS: Em funções Python, os parâmetros com valores default (padrão) DEVEM sempre estar no final da declaração.

# Erro!
# def teste(num=2, poten):

# Certo
def teste(poten, num=2):
    return num ** poten

# Outros exemplos

def soma(num1, num2):
    return num1 + num2

print(soma(4, 3))
# print(soma(4)) # TypeError
# print(soma()) # TypeError

# Exemplo mais complexo

def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu Pensei que você era o instrutor'
    return f'Olá {nome}'

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao('Ozzy'))

# Por quê utilizar parâmetros om valor default?

# - Nos permite ser mais flexíveis nas funções;
# - Evita erros com parâmetros incorretos;
# - Nos permite trabalhar com exemplos mais legíveis de código;

# Quais tipos de dados podemos utilizar como valores default para parâmetros?

# - Qual tipo de dado:
#   - Numeros, String, floats, booleanos, lista, tuplas, dicionarios, funções e etc;

# Exemplos
# def soma(num1, num2):
    # return a + b

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 2, subtracao))

# Escopo - Evitar problemas e confusões...

# Variáveis globais
# Variáveis locais

instrutor = 'Geek' # variável global

def diz_oi():
    instrutor = 'Python' # Variável local
    return f'Oi {instrutor}'

print(diz_oi())

# Se tivermos uma variável local com o mesmo nome de uma variável global, a local terá preferência.

def diz_oi():
    prof = 'Geek' # var Local
    return  f'Olá {prof}'

print(diz_oi())

# print(prof) # NameError

# ATENÇÃO com variáveis globais (Se puder evitar, evite!)

# Correto
total = 0

def incrementa():
    global total # Avisando que queremos ultilizar a variável global
    # total += 1 # UnboundLocalError (A variável local está sendo utilizada para processamento sem ter sido inicializada)
    total += 1 
    return total

print(incrementa())


# Podemos ter funções que são declaradas dentro de funções, e também tem uma
# forma especial de escopo de variável

def fora():
    contador = 0

    def dentro():
        nonlocal contador # puxa a variável do escopo da função fora()

        contador += 1
        return contador
    return dentro()

print(fora())
print(fora())
print(fora())
