"""
Argumentos somenete posicionais
"""


def cumprimentar(nome):
    print(f"Olá, {nome}!")


print(cumprimentar("geek"))
print(cumprimentar(nome="geek"))


def cumprimentar(nome, /, mensagem1="Olá", *, mensagem2):
    return f"{mensagem1} {nome} {mensagem2}"
    # / - argumentos posicionais
    # * - argumentos nomeados


print(cumprimentar("geek", mensagem1="Hello", mensagem2="tenha um bom dia"))
print(cumprimentar("geek", mensagem2="tenha um bom dia"))
print(cumprimentar("geek", "Hello", "tenha um bom dia"))  # aqui da erro
print(cumprimentar("geek", "Hello", mensagem2="tenha um bom dia"))  # aqui não da erro
