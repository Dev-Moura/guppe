"""
Modos de abertura de arquivo

r - > Abre para leitura - padrão
w - > Abre para escrita - sobrescreve caso o arquivo exista
x - > Abre para escrita somente se o arquivo não existir, caso exista, teremos um FileExistsError
a - > Abre para escrita no final do arquivo
+ ->  Abre para atualização (leitura e escrita)


OBS: abrindo no modo 'a' - append, se oarquivo não existir será criado. caso exista, o novo conteúdo
será adicionado SEMPRE ao final do arquivo. Com o modo 'a', não controlamos o cursor.


https://docs.python.org/3/library/functions.html#open

try:
    with open('university.txt', 'x') as arquivo:
        arquivo.write('Teste de conteúdo do arquivo. \n')
except FileExistsError:
    raise FileExistsError('Arquivo já existe, não posso criar')
"""

with open('frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite "sair): ')
        if fruta.lower() != 'sair':
            arquivo.write(f'{fruta}\n')
        else: 
            break

with open('outro.txt', 'r+') as arquivo:
    arquivo.seek(0)
    arquivo.write('linha ao top!\n')
    arquivo.write('nova !\n')
    arquivo.write('mais uma linha!\n')
