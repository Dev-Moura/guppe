"""
POO O método super()

oO método super() se refere à superclasse e permite acessar seus métodos e atributos.


"""


class Animal:
    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f"o {self.__nome} faz {som}")


class Gato(Animal):
    def __init__(self, nome, especie, raca):
        Animal.__init__(self, nome, especie)
        # super().__init__(nome, especie)
        super().faz_som("miau miau miau")
        self.raca = raca


felix = Gato("Felix", "Gato", "Siamese")
felix.faz_som("miau")
