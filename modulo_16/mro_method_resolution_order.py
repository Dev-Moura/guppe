"""
MRO - Method Resolution Order

Method Resolution ORder (Resolução de ordem de métodos), é a ordem de execução do métodos
(quem será executado primeiro).

Em python, a gente pode conferir a ordem de execução dos métodos (MRO) de 3 formas:
    - Via propriedade da classe __mro__
    - Via método mro()
    - Via help()
"""


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

    def cumprimentar(self):
        return f"pinguim"


# Testando

tux = Pinguim("tux")
tux.nadar()
tux.andar()
print(tux.cumprimentar())  # Method Resolution Order - MRO
