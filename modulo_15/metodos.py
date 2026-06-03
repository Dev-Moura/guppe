"""
POO - Métodos

- Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações
que este objeto pode realizar no seu sistema.

Em python, dividimos os métodos em 2 grupos: Métodos de instância
e métodos de classe.

# Métodos de instância:

# O método dunder init __init__ -> É um método especial chamado de construtor e sua função
é construir o objeto a partir da classe. Ou seja, sua função é criar os objetos

OBS: todos os elementos em python que inicia e finaliza com duplo underline é chamado de dunder (Double Underline)

OBS: Os métodos/funções dunder em python são chamados de métodos mágicos

ATENÇÃO! Por mais que possamos criar nossas próprias funções utilizando dunder, (underline no ínicio e no fim)
não é aconselhado, Python possui vários métodos com esta forma de nomeclatura e pode ser que mudemos o comportamento
dessas funções mágicas internas da linguagem. Então evite o máximo.

# Métodos são escritos em letras minúsculas, se for nome composto, as palavras são separadas por underline (Snake Case)

# Métodos de Classe em python são conhecidos como métodos estáticos em outras linguagens.
"""


class Lampada:
    
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
    
class ContaCorrente:
    
    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retornar o valor do produto com o desconto"""
        return (self.__valor * (100 - porcentagem)) / 100

    
from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:

    contador = 0

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)


    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"


    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False
    

nome = input("Digite o nome: ")
sobrenome = input("Digite o sobrenome: ")
email = input("Digite o email: ")
senha = input("Digite a senha: ")
confirma_senha = input("Confirme a senha: ")

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
    print("Usuário criado com sucesso!")
else:
    print("As senhas não conferem.")
    exit(42)

print(f'Usuario criado com sucesso!')

senha = input("Digite a senha para acesso: ")

if user.checa_senha(senha):
    print("Acesso concedido!")
else:
    print("Acesso negado! Senha incorreta.")
    exit(42)

print(f'Senha user criptografada: {user._Usuario__senha}')


from passlib.hash import pbkdf2_sha256 as cryp

# Métodos de Classe
# refatorando a ultima classe para utilizar métodos de classe
class Usuario2:

    contador = 0

    @classmethod
    def conta_usuario(cls):
        print(f'Classe: {cls}')
        print(f'Temos {cls.contador} usuário(s) no sistema')

    @classmethod
    def ver(cls):
        print('test')
    # O método de classe tem acesso a variável de classe, ou seja, a variável contador,
    # mas não tem acesso a variável de instância, ou seja, as variáveis nome, sobrenome, email e senha.


    @staticmethod
    def definicao():
        return 'Método estático não tem acesso a classe ou a instância, é apenas uma função dentro da classe.'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario2.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)    
        Usuario2.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')


    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"


    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False
    

    def __gera_usuario(self):
        return self.__email.split("@")[0]
    

# Método estático

print(Usuario2.contador)
print(Usuario2.definicao())

user = Usuario2('Michael', 'Guppe', 'michaelGuppe@gmail.com', '123456')

print(Usuario2.contador)
print(Usuario2.definicao())