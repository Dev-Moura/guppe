"""
Debuggando com PDB

PDB -> Python debugger

Vida de inseto - Life's Bug
Bug -> Inseto


"""
# OBS: A utilização do print() para debugar código é uma prática ruim

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        print(f'Ocorreu um problema: {err}')

print(dividir(4,0))

# A métodos profissionais de se fazer esse 'debug' utilizando o debugger
# Em python, podemos fazer isso de diferentes IDEs, como o pycharm ou utilizando 
# o PDB - Python Debugger

# exemplo com o pdb - python debugger

# Para utilizar o python debugger, precisamos* importar a bilioteca pdb e então utilizar a função set_trace()

# comandos básicos do PDB
# l (listar onde estamos no código)
# n (próxima linha)
# p (imprime a variável)
# c (continua a execução -  finaliza o debugging)

import pdb

nome = 'Angelina'
sobrenome = "jolie"
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = "Programação em Python: Essencial"
final = nome_completo + ' faz o curso ' + curso
print(final)


# Por quê utilizar esse formato?
# O  debug é utilizado duranto o desenvolvimento. Custumamos realizar todos os import de biliotecas
# no início do arquivo. Por isso, ao invés de colocarmos o import do pdb no início do arquivo,
# nós colocamos somente onde vamos deuggar, e ao finalizar já fazemos a remoção.


# A partir do python 3.7, não é mais necessário importar a biblioteca pdb, pois o comando de debug foi 
# incorporado como função built-in (integrada) chamada de breakpoint()

nome = 'Angelina'
sobrenome = "jolie"
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = "Programação em Python: Essencial"
final = nome_completo + ' faz o curso ' + curso
print(final)

# OBS: Cuidado com conflitos entre nomes de variáveis e os comandos do pdb

def soma(l, n, p, c):
    breakpoint()
    return l+ n +p + c

print(soma(1 , 3, 5, 7))

# como os nomes das variáveis são os mesmo dos comando pdb, devemos utilizar o comando p para 
# imprimir as variaveis. ou seja: p nome_da_variavel

# nada de colocar nomes não representativos em variáveis. Sempre optar por nomes significativos.

def soma(num1, num2, num3, num4):
    breakpoint()
    return(num1 + num2 + num3 + num4)