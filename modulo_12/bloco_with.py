"""
O bloco with

Passo para se trabalhar com arquivos:

1 - Abrirmos o arquivo
2 - Maniipula o arquivo
3 - fechamos o arquivo

O bloco with é utilizado para criar um contexto de trabalho onde os recursos
são gerenciados automaticamente. Ele garante que o arquivo seja fechado corretamente,
mesmo que ocorra um erro durante a manipulação do arquivo.

arquivo = open('texto.txt')

"""

# o bloco with - forma Pythônica de manipular arquivos

with open('arquivo.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed())


# print(arquivo.read())

print(arquivo.closed())

