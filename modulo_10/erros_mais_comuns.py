"""
Erro mias comuns em python

Os erros mais comuns:

1 - SyntaxError -> Ocorre qunado o Python encontra um erro de sintaxe. Ou seja, vocÊ escreveu algo que o 
python não reconhece como parte da linguagem.

Exemplos SyntaxError

a - def funcao:
        print('geek')
    
b - def = 1

c - return

2 - NameError -> Ocorre quando uma variável ou função não foi definida.

Exemplos NameError

a - print(geek)


3 - TypeError -> Ocorre qunado uma função/operação/ação é aplicada a um tipo errado.

Exemplos TypeError

a -
    print(len(5)) 

b - 
    print('Geek' + [])

c -
    print('geek' + 4)


4 - IndexError -> Ocorre quando tentamos acessar um elmento em uma lista ou outro tipo de dado 
indexado utilizando um índice inválido.

a -
    lista = ['geek']
    print(lista[2])

b - 
    lista = ['geek']
    print(lista[0][10])

c - 
    tupla = ['geek']
    print(lista[0][10])

5 - ValueError -> Ocorre quando uma função/operação built-in (integrada) recebe um argumento com tipo correto mas valor inapropriado.

Exemplo ValueError

a -
    print(int('geek'))

6 - KeyError -> Ocorre quando tentamos acesar um dicionário com uma chave que não existe.

Exemplo keyError

a -
    dic = {'Python': 'university'}
    print(dic['geek'])

7 - AttributeError ->  Ocorre qunado uma variável não tem um atributo/função

Exemplos AttributeError

a - 
    tupla = (11, 2, 31, 4)

    print(tupla.sort())

8 - IndentationError -> Ocorre quando não respeitamos a identação do python (4 espaços)

Exemplos IdentationError

a -
def nova():
print('geek')

b -
for i in range(10):
i+1

OBS: Exceptions e Erros são sinônimos na programação

OBS: Importante ler e prestar atenção na sáida de erro.

"""



