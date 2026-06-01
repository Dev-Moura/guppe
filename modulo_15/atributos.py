"""
POO - Atributos

Atributos -> Representam as caracteristicas do objeto. Ou seja, pelos atributos
nos conseguimos representar computacionalmente os estados de um objeto.

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de instancia;
    - Atributos de Classe;
    - Atributos de Dinamico;

# Atributos de instancia: sao atributos declarados dentro do metodo construtor.

OBS: metodo construtor: E um metodo especial utilizado para construçao do objeto.

# Em python, por convençao, ficou estabelecido que, atributos de uma classe e publico.
ou seja, podem ser acessado em todo o projeto.
Caso queiramos demonstrar que determinado atributo, deve ser tratado com privado, ou seja,
que deve ser acessado/utilizado somente dentro da propria classe onde esta declarado,
utiliza-se __ duplo underscore no inicio de seu nome.

conhecido como Name Mangling.
"""
from math import prod

from modulo_15.classes import valor


# Classes com Atributos de instacias publicas
class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.power = False

class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

class Produto:
    def __init__(self, nome, decricao, valor):
        self.nome = nome
        self.decricao = decricao
        self.valor = valor

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

# Atributos Privados

class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)


# OBS: Lembre-se que isso e apenas uma convençao, ou seja, a lingaguem python nao
# vai impedir que façamos acesso ao atriutos sinalizados como privados fora da classe.

# Exemplo

user = Acesso('user@gmail.com','123456')

print(user.email)

# print(user.__senha) # AttributeError

print(user._Acesso__senha) # Temos acesso. Mas Nao deveriamos fazer este acesso (Name Mangling)

print(dir(user))

user.mostra_senha()
user.mostra_email()

# Oque significa atributos de instancia?

# Significa, que ao criarmos instancias/objetos de uma classe, todas as instancias
# terao estes atributos.

user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '987654')

user1.mostra_email()
user2.mostra_email()

# Atributos de Classe

# Atributos de classe, sao atributosm claro, que sao declarados diretamente na classe, ou seja,
# fora do construtor, Geralmente ja inicializamos um valor, e este valor e compartilhado entre
# todas as insancias da classe. ou seja, ao inves de cada instancia da classe ter seus proprios
# valores como e o caso dos atributos de instancia, com os atributos de classe todas as instancias
# terao o mesmo valor para este atributo.

# Refatorando a classe produto

class Produto:

    # Atributo e classe
    imposto = 1.05 # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id



p1 = Produto('PlayStation 4 ' ,'Video Game', 2300)
p2 = Produto('Xbox S ' ,'Video Game', 4500)

print(p1.valor) # Acesso possivel, mais incorreto de um atributo de classe
print(p2.valor)

# OBS: Nao precisasmos criar uma instancia de uma classe para fazer acesso a um atributo de classe

# print(dir(Produto))
print(Produto.imposto) # Acesso correto de um atributo de classe

print(p1.id)
print(p2.id)

# OBS: Em Linguagens como o java, os atributos conhecidos como atributos de calsse aqui em python
# sao chamado de atributos estaticos;


# Atributos Dinamicos -> Um atributos de instancia que pode ser criada em tempo de execuçao.

# OBS: O Atributo dinamico sera exclusivo da instancia que o criou

p3 = Produto('PlayStation 4 ' ,'Video Game', 2300)
p4 = Produto('Arroz' ,'Mercearia', 5.99)


# Criando um atributo dinamico em tempo de execuçao

p4.peso = '5kg'

print(f'Produto: {p4.nome}, Descriçao: {p4.descricao}, valor: {p4.valor}, Peso: {p4.peso}')

# Deletando atributos

print(p3.__dict__)
print(p4.__dict__)

del p4.peso

print(p3.__dict__)
print(p4.__dict__)
