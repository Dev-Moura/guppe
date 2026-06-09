"""
POO - Propriedades (properties)

Em linguagens de programação orientadas a objetos, ao declararmos atributos privados nas classes,
costumamos a criar métodos públicos para manipulação desses atributos. Esses métodos são chamados de getters e setters.
onde os getters retornam o valor do atributo e os setters definem o valor do atributo.

estilo semelhante ao java

class Conta:
    contador = 0

    def __init__(self, titular, saldo, limite) -> None:
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f"Saldo de {self.__saldo} do titular {self.__titular}"

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente")

    def transferir(self, destino, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            destino.depositar(valor)
        else:
            print("Saldo insuficiente")

    def get_numero(self):
        return Conta.contador

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite


conta1 = Conta("João", 1000, 5000)
conta2 = Conta("Maria", 2000, 10000)

print(conta1.extrato())
print(conta2.extrato())


soma = conta1.get_saldo() + conta2.get_saldo()
print(f"A soma do saldo das contas é {soma}")

print(conta1.__init__)
conta1.set_limite(10000)
print(conta1.__dict__)


"""


class Conta:
    contador = 0

    def __init__(self, titular, saldo, limite) -> None:
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property
    def numero(self):
        return Conta.contador

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        return f"Saldo de {self.__saldo} do titular {self.__titular}"

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente")

    def transferir(self, destino, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            destino.depositar(valor)
        else:
            print("Saldo insuficiente")

    def valor_total(self):
        return self.__limite + self.__saldo


conta1 = Conta("João", 1000, 5000)
conta2 = Conta("Maria", 2000, 10000)

print(conta1.extrato())
print(conta2.extrato())

soma = conta1.saldo + conta2.saldo
print(f"A soma do saldo das contas é {soma}")

print(conta1.__dict__)
conta1.limite = 76543
print(conta1.__dict__)
print(conta1.limite)

print(conta1.valor_total())
