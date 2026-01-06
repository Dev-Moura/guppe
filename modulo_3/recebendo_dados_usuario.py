"""
Recebendo dados do usuario

# Exemplo de print 'antigo' 2.x
# print('Seja bem-vindo(a) %s' % nome)

# Exemplo de print 'moderno' 3.x
# print("seja bem-vindo(a) {0}".format(nome))

# Exemplo de print 'atual' 3.7
# print(f'Seja bem vindo {nome}')

input() -> Todos os dados recebido via input é do tipo String
"""
# entrada de dados
nome = input('Digite seu nome: ')

print(f'Seja bem vindo {nome}')

idade = int(input('Digite sua idade: '))

# saida de dados

print(f'O {nome} tem {idade} anos')

#  O cast é a conversão de um tipo de dado para outro.
print(f'O {nome} nasceu em {2026 - int(idade)}')