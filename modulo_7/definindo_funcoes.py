"""
Definindo funções

- Funções são pequenos trechos de código que realizam tarefas específicas;
- Pode ou não receber entrada de dados e retornar um sáida de dados;
- São muito uteis para executar procedimentos ismilares por repetidas vezes;

OBS: se você escrever um função que realiza várias tarefas dentro dela;
é bom fazer uma verificação para que a função seja simplificada.

# Em python a forma geral de definir uma função é:

def nome_da_funcao(parametros_De_entrada):
    Bloco_da_funcao

Onde:

nome_da_funcao -> SEMPRE, com letras minúsculas, e se for nome composto, separados por underline (Snake Case);
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não;
bloco_da_funcao -> Também chamado de corpo da função ou implementação, é ode o processamento da função acontece.
Nete Bloco, pode ter ou ão retorno da função.

OBS: Veja que para definir função, utilizamos a palavra reservada 'def' informando ao Python que
estamos definindo uma função. Também abrimos o bloco de código com o já conhecido dois pontos: que é
utilizado em python para definir blocos
"""

# Exemplo de utilização de função

cores = ['verde', 'amarela', 'azul', 'branco']

# Utilizando a funão integrada (Built-in) do python print()

print(cores)

curso = 'programação em python: Essencial'

print(curso)

cores.append('azul')

print(cores)

# curso.append('mais dados...') # AttributeError
# print(curso)

# cores.clear()
# print(cores)
#
# print(help(print))

# DRY - Don't Reapet Yoourself - Não repita você mesmo / não repita seu código.

# Mas então como definir funções?

def diz_oi():
    print("Oi!")

# Chamada de execução
diz_oi()

# OBS: 1 - Veja que, dentro das nossas funções podemos utilizar outras funções;
# 2 - Veja que nossa função só executa 1 tarefa, ou seja, a única coisa que ela faz é dizer oi;
# 3 - Veja que ela não recebe nenhum parâmetro de entrada;
# 4 - Veja que está função não retorna nada;

def cantar_parabens():
    print('Parabens! pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('muitos anos de vida')
    print('Viva o aniversariante!')

for i in range(5):
    cantar_parabens()

# Em python, podemos inclusive criar variáveis do tipo de uma função e executar esta função através da variável
canta = cantar_parabens
canta()
