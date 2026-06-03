"""
POO - Objetos

Objetos -> São instâncias da classe. Ou seja, após o mapeamento do objeto do mundo real para sua 
representação computacional, devemos poder criar quantos objetos forem necessários. Podemos pensar
nos objetos/instâncias de uma classe como variáveis do tipo definido na classe.

"""

class Lampada:


    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


    def checa_lampada(self):
        return self.__ligada
    

    def ligar_desligar(self):
        if self.__ligada:
            self.__liagada = False
        else:
            self.__ligada = True


class Cliente:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf


    def diz(self):
        return f'O cliente é {self.__cliente._Cliente__nome}'

class contaCorrente:
    
    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = contaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        contaCorrente.contador = self.__numero

    def mostrar_cliente(self):
        print(f'Cliente: {self.__cliente._Cliente__nome}')

class Usuario:

    def __init__(self, nome, email, senha):
        self.__nome = nome
        self.__email = email
        self.__senha = senha

lamp1 = Lampada('Branca', 220, 60)

lamp1.ligar_desligar()

print(f'A lâmpada está ligada? {lamp1.checa_lampada()}')

cc1 = contaCorrente(5000, 20000)

user1 = Usuario('Felicity', 'jones', 'felicity@gmail.com', '123456f')

nome = 'Angelina'
sobrenome = 'Jolie'
email = 'angelina@gmail.com'
senha = '123456'

user = Usuario(nome, sobrenome, email, senha)

cliente2 = Cliente('Brad Pitt', '123456789-00')

cc2 = contaCorrente(10000, 50000, cliente2)

cc2.mostrar_cliente()

cc2.__ContaCorrente__cliente.diz()