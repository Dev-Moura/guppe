"""
POO - Herança Múltipla

Herança múltipla é quando uma classe herda de mais de uma classe.
fazendo com que a classe filha tenha acesso a todos os atributos e métodos das classes pai.


# A herança múltipla pode ser feita de duas formas:
 - por multiderivação direta
 - por multiderivação indireta



class base1:
    pass


class base2:
    pass


class Multiderivada(base1, base2):
    pass


# exemplo de multiderivação indireta


class base1:
    pass


class base2(base1):
    pass


class base3(base2):
    pass


class Multiderivada(base3):
    pass

Não importa se a derivação é direta ou indireta. A classe filha herda todos os atributos e métodos das classes pai.

"""

from string import printable


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        print(f"Olá, meu nome é {self.__nome}")


class Aquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        print(f"{self._Animal__nome} está nadando")

    def cumprimentar(self):
        return f"Eu sou {self._Animal__nome} do mar"


class Terrestre(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        print(f"{self._Animal__nome} está andando")

    def cumprimentar(self):
        return f"Eu sou {self._Animal__nome} da terra"


class Pinguim(Terrestre, Aquatico):
    def __init__(self, nome):
        super().__init__(nome)


# Testando

baleia = Aquatico("Wally")
baleia.nadar()
print(baleia.cumprimentar())

tatu = Terrestre("Xim")
tatu.andar()
print(tatu.cumprimentar())

pinguim = Pinguim("tux")
pinguim.nadar()
pinguim.andar()
print(pinguim.cumprimentar())  # Method Resolution Order - MRO


# Objeto é instância de...


print(f"isinstance(pinguim, Pinguim): {isinstance(pinguim, Pinguim)}")
print(f"isinstance(pinguim, Aquatico): {isinstance(pinguim, Aquatico)}")
print(f"isinstance(pinguim, Terrestre): {isinstance(pinguim, Terrestre)}")
print(f"isinstance(pinguim, Animal): {isinstance(pinguim, Animal)}")
print(f"isinstance(pinguim, object): {isinstance(pinguim, object)}")
