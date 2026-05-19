"""
Seek and Cursors

seek() -> É utilizado para movimentar o cursor pelo arquivo.
"""
arquivo = open('texto.txt')
arquivo2 = open('texto.txt')
# Seek() -> A função seek() é utilizada para movimentação do cursor
# Movimentando o cursor pelo arquivo com a função seek()
arquivo.seek(21)
print(arquivo.read())

# readline() -> Função que lê o arquivo linha a linha (readline -> lê linha)
ret = arquivo.readline()
print(type(ret))
print(ret)

# readlines() -> Função que lê o arquivo e retorna uma lista com as linhas do arquivo (readlines -> lê linhas)
linhas = arquivo2.readlines()
print(len(linhas))
print(type(linhas))
print(linhas)  

# OBS: Quando abrimos uma rquivo com a função open() é criada uma conexão entre o arquivo
# no disco do computador e o nosso programa. Essa conexão é chama de streaming. Ao finalizar
# os trabalhos com o arquivo devemos fechar essa conexão. Para isso utilizamos a função close()

# 1 - Abrir o arquivo;
arquivo.open('texto.txt')

# 2 - trabalhar o arquivo;
print(arquivo.read())

# verifica se o arquivo está aberto ou fechado
# retorno aqui vai ser False, pois o arquivo está aberto
print(arquivo.closed)

# 3 - Fechar o arquivo;
arquivo.close()

# retorno aqui vai ser True, pois o arquivo está fechado
print(arquivo.closed)

print(arquivo.read())  # ValueError: I/O operation on closed file.

# OBS: Se tentarmos manipular o arquivo após fechá-lo, teremos um ValueError, pois o arquivo
# já foi fechado e não podemos mais realizar operações de leitura ou escrita nele.


arquivo= open('texto.txt')
# Com a função read() podemos limitar a quantidade de caracteres a serem lidos no arquivo
print(arquivo.read(50))