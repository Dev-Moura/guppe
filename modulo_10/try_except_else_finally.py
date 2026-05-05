"""
try / except / else / finally

Dica de quando e onde tratar o código

TODA ENTRADA DEVE SER TRATADA!

OBS: A Função do usuário é destruir o sistema.

# Else -> É Executado somente se não ocorrer o erro.

"""

num = 0

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {num}')


# Finally

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Você não digitou um valor válido.')
else:
    print(f'Você digitou {num}')
# OBS: O bloco finally é sempre executado. Indedente se houve exceção ou não.
finally:
    print('Executando o finally')

# O finally, geralmente é utilizado para fechar ou desalocar recursos.

# Exemplo mais complexo ERRADO

def dividir(a,b):
    return a / b

num1 = int(input('informe o primeiro número: '))

try:
    num2 = int(input('Informe o segundo número: '))
except ValueError:
    print('O valor precisa ser numérico')

try:
    print(dividir(num1, num2))
except NameError:
    print('Valor incorreto')

# Exemplo complexo CORRETO
# OBS: Você é responsável pelas entradas das suas funções. Então, trate-as!

def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        print('Valor incorreto')
    except ZeroDivisionError:
        return 'Não é possível realizar divisão por zero'


num1 = input('informe o primeiro número: ')
num2 = input('Informe o segundo número: ')
0

print(dividir(num1, num2))

# Tratamento semi-genérico


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        print(f'Ocorreu um problema: {err}')


num1 = input('informe o primeiro número: ')
num2 = input('Informe o segundo número: ')
0

print(dividir(num1, num2))