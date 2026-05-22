"""
Escrevendo em arquivos


OBS: Ao abrir um arquivo para leitura ,Não podemos ealizar a escrita nele. apenas ler.
da mesma forma, se abrirmos um arquivo para escrita, não podemos realizar a leitura nele, apenas escrever.

Ao subir um arquivo para escrita, se o arquivo não existir, ele será criado. Caso o arquivo exista,
o conteúdo anterior será apagado e substituído pelo novo conteúdo.

para escrevermos dados em um aruivo, após abrir o arquivo, utilizamos a função write()
Esta função recebe uma string como parâmetro. Caso o contrário teremos um TypeError
 

"""

# forma Pythonica de escrita com with - modo 'w' - write - escrita
with open('novo.txt', 'w') as arquivo:
    arquivo.write('Escrevendo dados em arquivo.\n')
    arquivo.write('podemos colocar quantas linhas quisermos.\n')
    arquivo.write('ultima linha.\n')


with open('teste.py', 'w') as arquivo:
    arquivo.write('print("Hello, World!")')


# forma não pythonica de escrita em arquivos - tradicional
arquivo = open('mais.txt', 'w')

arquivo.write('Escrevendo dados em arquivo.\n')
arquivo.write('podemos colocar quantas linhas quisermos.\n')

arquivo.close()

with open('geek.txt', 'w') as arquivo:
    arquivo.write('Geek University - Programação em Python: Essencial \n' * 100)


with open('frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite "sair): ')
        if fruta.lower() != 'sair':
            arquivo.write(f'{fruta}\n')
        else: 
            break
