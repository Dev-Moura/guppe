"""
Sistema de arquivos - Manipulaçao

"""
import os
from os import mkdir
from os.path import exists
from traceback import print_tb

# Paths relativos
print(os.path.exists('name_user'))
print(os.path.exists('name_user/university'))
print(os.path.exists('outro'))

# Paths absolutos
print(os.path.exists('/home/name_user/university'))
print(os.path.exists('/home/name_user/Imagens'))
print(os.path.exists('/home/name_user/Imagens/wallpaper2.png'))

# Criando arquivos

# forma 1
open('arquivo-teste.txt', 'w').close()

# forma 2
open('arquivo-teste2.txt', 'w').close()

# forma 3
with open('arquivo-teste3.txt', 'w') as arquivo:
    pass

os.mknod('arquivo.test4.txt')

os.mknod('/home/name_user/university.txt')

# Se voce estiver utilizando no mac os, pode haver um erro de permissionError

# Se criando um arquivo via mknod, se o arquivo ja existir teremos o erro fileExistsError

# path relativo
os.mkdir('templates')

# Criando multi-dirtorios
os.makedirs('templates/geek/university')
# se ja existir da erro

os.makedirs('templates2/novo2/outro2', exist_ok=True )

# Renomear diretorios

os.rename('templates2', 'geek2')

# Se o diretorio nao existir teremos um FileNotFoundError

# Se e diretorio que queremos renomear nao estiver vazio, teremos um OSerror

os.rename('novo.txt', 'novo2.txt')

os.rename('/home/name_user/template/novo.txt', '/home/name_user/template/novo2.txt')


# ATENCÇAO! Tome cuidado com os comandos de deleçao. Ao deletarmos um arquivo ou diretorio, eles
# nao vao para a lixeira. eles somem.

os.remove('/home/name_user/template/novo2.txt')

# Se voce estiver no Windows e o arquivo que voce for deletar estiver me uso, voce tera um erro.
# Caso o arquivo nao exista, teremos o fileNotFoundError
# Se voce informar um diretorio ai nves de um arquivo vai dar um IsADirectoryError


os.rmdir('templates12')

# Se o diretorio tiver qualquer conteudo teremos um OSError
# Se o diretorio Nao existir teremos um fileNotFoundError

# removendo uma arvore de arquivos
for d in os.scandir('geek2'):
    print(f'- {d.name}')
    if d.is_file():
        os.remove(d.name)


# removendo uma arvore de diretorios vazios

os.removedirs('geek2/outro/mais')

# ATENCA: remover arquivos e diretorios com python, nao os joga na lixeira, ele deleta do sistema direto

from send2trash3k import send2trash3k

os.remove('cesta1.txt') # Nao vai para a lixeira. E deletado imediatamente

send2trash3k('cesta2.txt') # vai pra lixeira. Pode ser restaurado

# trabalhando coma rquivos e diretorios temporarios

import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretorio temporario em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as f:
        f.write('testando\n')
    input()

# Estamos criando um diretorio temporario. abrindo o mesmo e dentro dele criando
# um arquivo para escrevermos um texto. No final, usamos um input() so para mantermos
# os arquivos temporarios 'vivos' dentro dos blocos with

# OBS: possivelmente, o codigo acima nao ira funcionar se voc estiver utilizando
# o windows. por conta desse sistema trabalhar de forma diferente com arquivos
# temporarios.


# Trabalhando com diretorios temporarios

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University\n')
    tmp.seek(0)
    print(tmp.read())

# so conseguuimos escrever bits. por isso utilizamos b''

# sem o bloco with

arquivo= tempfile.TemporaryFile()
arquivo.write(b'Geek University\n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()


arquivo= tempfile.NamedTemporaryFile()
arquivo.write(b'Geek University\n')
print(arquivo.name)
print(arquivo.read())
input() # pra segurar o terminar e vizualizar o nome
arquivo.close()