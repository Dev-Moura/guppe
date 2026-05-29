"""
- Decorators com diferentes assinaturas
- Decorator Pattern
- A assinatura de uma funçao e representada pelo seu retorno, nome e parametros de entrada.
"""

# relembrando

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper() # vai aplicar em toda funçao
    return aumentar

@gritar
def saudar(nome):
    return f'Ola, eu sou o/a {nome}'

@gritar
def ordenar(principal, acompanhamento):
    return f'Ola, eu gostaria de {principal}, acompanhando de {acompanhamento}, por favor.'

print(ordenar("Picanha", "Batata Frita"))
print(saudar('Flavio'))

@gritar
def lol():
    return f'lol'

print(lol())
# Vale lembrar que podemos utilizar parametros nomeados

print(ordenar(principal="Picanha", acompanhamento="Batata Frita"))

# Decorator com argumentos

def verfica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna

@verfica_primeiro_argumento('pizza')
def comida_favorita(*args):
    return args

@verfica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


print(soma_dez(10, 12))

print(comida_favorita('pizza' , 'Churrasco'))

print(comida_favorita('sanduiche', 'churrasco'))
