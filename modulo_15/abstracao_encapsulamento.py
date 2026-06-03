"""
POO - Abstração e Encapsulamento

O objetivo da POO é encapsular o nosso código dentro de um grupo lógico e hierárquico utilizando
classes.

Encapsulamento -> é o ato de esconder os dados dentro de uma classe, ou seja, tornar os atributos privados. Desta

Abstração -> abstrair, ou seja, representar algo complexo de forma mais simples. A abstração

Exemplo - Acessando elementos privados fora da classe:

instancia._Pessoa__nome

instancia._Pessoa__falar()

Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos
privado de usuário.

"""

class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'O saldo do cliente {self.__titular} é de R${self.__saldo} com limite de R${self.__limite}')


    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('Valor inválido para depósito.')

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print('Valor inválido para saque ou saldo insuficiente.')


    def transferir(self, valor, conta_destino):
        # 1 - remover o valor da conta de origem
        self.__saldo -= valor
        self.__saldo -= 5.99 # Taxa de transferencia

        # 2 - Adicionar o valor na conta de destino
        conta_destino.__saldo += valor





conta1 = Conta('Michael', 1500, 5000)
conta1.extrato()


conta2 = Conta('Maria', 2000, 6000)
conta2.extrato()

conta2.transferir(500, conta1)

conta1.extrato()
conta2.extrato()