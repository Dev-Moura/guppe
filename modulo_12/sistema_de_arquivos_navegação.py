"""
Sistema de Arquivos de avegaçao

para fazer uso de manipulaçao de arquivos do sistemas operaciona, precisamos importar
e fazer o uso do modulo os.

os -> operating system - sistema operacional

"""

# fazer o import
import os

import sys

#getcwd() ->  pega o current work directory - diretorio de trabalho corrent
# Retorna o path (caminho) absoluto
print(os.getcwd()) # /media/sf_documents/vm/PycharmProjects/guppe
os.chdir('..')

print(os.getcwd()) # /media/sf_documents/vm/PycharmProjects
os.chdir('..') # Para mudar o diretorio, podemos utilizar o chdir()

print(os.getcwd()) # /media/sf_documents/vm/
os.chdir('..')

print(os.getcwd()) # /media/sf_documents
os.chdir('..')

print(os.getcwd()) # /media/
os.chdir('..')

print(os.getcwd())

# Podemos checar se um diretorio e absoluto ou relativo

print(os.path.isabs('/home/michael/')) # True

# OBS para qunado for trabalhar com ruindows
# se voce, infelizmente, estiver ut-ilizando um computador com ruindows,
# tera que ter cuidado ao verificar diretorios

print(os.path.isabs('C:\\Users\\name_user\\ruindows\\'))

# Podemos indenticar o SO pelo os
print(os.name)
print(os.uname())
print(sys.platform)

# 'home/user/workspace/sistema'

print(os.getcwd()) #  /media/sf_documents/vm/PycharmProjects/guppe

res = os.path.join(os.getcwd(), 'michaeldesktop')

os.chdir(res)

print(os.getcwd()) # /media/sf_documents/vm/PycharmProjects/guppe/michael

# veja que o os.path.join() recebe dois parametros, sendo o primeiro diretorio atual e o segundo o
# diretorio que sera juntado ao atual

# listando os diretorios com o listdir

print(os.listdir())
print(len(os.listdir()))

print(os.listdir('/etc'))

# podemos listar os arquivos e diretorios com mais detalhes com scandri()

scanner = os.scandir()

arquivos = list(scanner)

print(arquivos)

print(dir(arquivos[0]))

print(arquivos[0].inode())
print(arquivos[0].is_dir())
print(arquivos[0].is_file())
print(arquivos[0].is_symlink())
print(arquivos[0].name)
print(arquivos[0].path)
print(arquivos[0].stat())

# OBS: Quando utilizamos a funçao scndir() nos precisamos fecha-la, assim quando abrimos um arquivo

scanner.close()