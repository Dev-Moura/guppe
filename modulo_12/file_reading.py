"""
Leitura de Arquivos


Para o conteúdo de um arquivo em python, utilizamos a função integrada open(),
que literamente significa "abrir".

open() -> A Forma mais simples de utilização nós passamos apenas um parâmetro de entrada,
que neste caso é o caminho para o arquivo a ser lido. essa função retorna um _io.TextIOWrapper.
e é com ele que trabalhamos então.


https://docs.python.org/3/library/functions.html#open


# OBS: Por padrão, a função open() abre o arquivo para leitura. Este arquivo
deve existir, ou então teremos o erro FileNotFoundError

modo r -> read -> leitura
modo w -> write -> escrita (sobrescreve o arquivo)
modo x -> create -> criação (gera um erro se o arquivo já existir)
modo a -> append -> acrescentar (mantém o conteúdo e acrescenta novas informações ao final
modo b -> binary -> binário (para arquivos não textuais, como imagens e arquivos executáveis)
modo t -> text -> texto (padrão, para arquivos de texto)

"""

arquivo = open('texto.txt')

# print(arquivo)

# print(type(arquivo))

# Para ler o conteúdo de um arquivo, utilizamos a função read()

ret = arquivo.read()

print(type(ret))

print(ret)  

# OBS: O python, utiliza um recurso para trabalhar coma rquivos chamado cursor. esse cursor,
# funciona como o cursor quando estamos escrevendo.

# print(arquivo.read())


