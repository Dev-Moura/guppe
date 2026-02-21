"""
Docstring for modulo_7.kwargs_funcoes

**Kwargs

Poderíamos chamar este parâmero de **xis, mas por convenção chamamos de **kwargs

Este é só mais um parâmero, mas diferente do *args que coloca os valores extras em uma tupla,
o **kwargsexige que utilizemos parâmetros nomeados, e tranforma esses parâmetros extras em um dicionário.
"""

# Exemplo 

def cores_favoritas(**kwargs):
  for pessoa, cor in kwargs.items():
    print(f'A cor favorita de {pessoa.title()} é {cor}')

cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# OBS: Os parâmetros *args e **kwargs não são obrigatórios.

cores_favoritas()

cores_favoritas(geek='navy')

# Exemplos mais complexo

def cumprimento_especial(**kwargs):
  if'geek' in kwargs and kwargs['geek'] == 'python':
     return 'Você recebeu um cumprimento Pythônico Geek!'
  elif 'geek' in kwargs:
    return f"{kwargs['geek']} Geek!"
  return 'Não tenho certeza quem você é....'

print(cumprimento_especial())
print(cumprimento_especial(geek="Python"))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='Especial'))


# Nas nossas funções, podemos ter (Nesta Ordem):

# - Parâmetros obrigatórios;
# - *args;
# - Parâmetros default (Não obrigatórios);
# - **Kwargs

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
  print(f'{nome} tem {idade} anos') # parâmetros obrigadtorios
  print(args) # args
  if solteiro: # defaults
    print('Solteiro')
  else:
    print('Casado')
  print(kwargs) # kwargs


minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', você='Vai')
minha_funcao(19, 'Carla', java=False, python=True)

# Entenda por que é importante manter a ordem dos parâmtros na declaração

# Função com a ordem correta de parâmetros
def mostra_info(a ,b, *args, instrutor='geek', **kwargs):
  return [a, b, args, instrutor, kwargs]

# função com a ordem incorreta de parâmetros
# def mostra_info(a ,b, instrutor='geek', *args, **kwargs):
#   return [a, b, args, instrutor, kwargs]

"""
a = 1 
b = 2
args = 3
instrutor = 'Geek'
kwargs = {'sobrenome': 'university', 'cargo': 'Instrutor'}

"""

print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))

# Desempacotar com **kwargs 

def mostra_nomes(**kwargs):
  return f"{kwargs['nome']} {kwargs['sobrenome']}"

nome = {'nome' : 'Felicity', 'sobrenome': 'Jones'}

print(mostra_nomes(**nome))

def soma_multiplos_numeros(a, b, c):
  return a + b + c

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3)

# OBS! Os nomes da chave em um dicionário devem ser o mesmo dos parâmetros da função

# dicionario = dict(d=1, e=2, f=3) # TypeError
# soma_multiplos_numeros(**dicionario)

soma_multiplos_numeros(**dicionario, fang='Python')