"""
O block try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. 
Previnindo assim que o programa pare de funcionar e o usuário mreceba mensagens de erro inesperadas.

A forma geral mais simples é: 

try:
    //execução problemática
except:
    // oque deve ser feito em caso de problemas

"""

# Exemplo 2 - Tratando um erro genérico

try:
    geek()
except:
    print("Deu problema")

# Tente executar a função geek(), caso você encontre erros, imprima a mensagem de erro.

# OBS:Tratar erro de forma genérica não é uma boa prática. O ideal é SEMPRE tratar de forma específica.

# Exemplo 3 - tratando um erro específico

try:
    geek()
except NameError:
    print("Você está utilizando uma função inexistente")

# Exemplo 4 - tratando um erro específico 

try:
    len(5)
except TypeError:
    print("Você está utilizando uma função inexistente")

# Exemplo 5 - tratando um erro específico com detalhes do erro

try:
    len(5)
except TypeError as err:
    print(f"A aplicação gerou o seguinte erro: {err}")

# Podemos efetuar diversos tratamentos de erros de uma vez.

try:
    # len(0)
    # print("geek"[9])
    geek()
except NameError as err1:
    print(f"Deu NameError: {err1}")
except TypeError as err2:
    print(f"Deu TypeError: {err2}")
except:
    print(f"Deu um erro diferente")


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None
    
dic = {"nome": "geek"}


print(pega_valor(7, "geek"))
print(pega_valor(dic, 8))
