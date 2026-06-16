"""
Assertion (Afirmações/Checagens/Questionamentos)

Em python utilizamos a palavra reservada 'assert' para realizar simples afirmações utilizadas no
testes.

utilizamos 'assert' em uma expressão que queremos checar se é válida ou não.
Se a expressão for verdadeixa, retorna None e caso seja falsa, levanta um erro
do tipo AssertionError.

# OBS: Nós podemos especificar qual opcionalmente, um segundo  argumento ou mesmo uma mensagem de erro personalizada.

# OBS: a palavra 'assert' pode ser utilizada em qualquer função ou código nosso.

# ALERTA: cuidado ao utilizar 'assert'
Se um programa Python for executado com o parâmetro -O, nenhum assertion será valido, ou seja,
todos os seus asserts serão ignorados.

"""


def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, "Ambos números precisam ser positivos"
    return a + b


def comer_fast_food(comida):
    assert comida in [
        "Pizza",
        "Hambúrguer",
        "Sushi",
    ], "A comida precisa ser Pizza, Hambúrguer ou Sushi"
    return f"Eu estou comendo {comida}"


comida = input("informe a comida: ")
resultado = comer_fast_food(comida)
print(resultado)


def funcao_ruim():
    assert usuario.eh_admin, "Somente administradores podem executar esta função"
    destroi_todo_o_sistema()
    return "R.I.P"
