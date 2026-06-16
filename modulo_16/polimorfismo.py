"""
POO - Polimorfismo

Poli -> Muitas
Morfis -> Formas

Quando a gente reimplementa um método presente na classe pai em classes filhas
estamos realizando uma sobrescrita de método(overriding)

O overriding é a melhor representação do polimorfismo
"""


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError("A classe filha precisa implementar esse método")

    def comer(self):
        print(f"{self.__nome} está comendo...")


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f"{self._Animal__nome} fala: Au Au!")


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f"{self._Animal__nome} fala: Miau!")


class Rato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f"{self._Animal__nome} fala: qui qui!")


# Teste

felix = Gato("Felix")
felix.comer()
felix.falar()

rex = Cachorro("Rex")
rex.comer()
rex.falar()

rato = Rato("Rato")
rato.comer()
rato.falar()
