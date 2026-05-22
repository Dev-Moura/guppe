"""
StringIO

ATENÇÃO: Para ler ou escrever dados em arquivos do sistema operacional, o software precisa
ter permissão:
    - Para ler um arquivo, o software precisa de permissão de leitura.
    - Para escrever em um arquivo, o software precisa de permissão de escrita.
    - Para criar um arquivo, o software precisa de permissão de escrita no diretório onde o arquivo será criado.

    
StringIO -> Utilizado para ler e criar arquivos em memória.


"""

# Primeiro importamos o stringIO do módulo io
from io import StringIO

mensagem = 'Esta é uma string normal'

# Podemos criar uma rquivo em memória já com uma string
# inserida ou mesmo vazio para inserirmos texto depois

arquivo = StringIO(mensagem)

print(arquivo.read())  # Lê o conteúdo do arquivo em memória

# escrevendo outros textos
arquivo.write(' Outro texto')


# podemos moviemntar o cursor
arquivo.seek(0)  # Move o cursor para o início do arquivo

print(arquivo.read())  # Lê o conteúdo atualizado do arquivo em memória