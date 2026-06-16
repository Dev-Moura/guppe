"""
Conhecendo o módulo pickle

A função o Pickle é realizar o seguinte processo:

Objeto Python -> Binarização

Binarização -> Objeto Python

este processo é chamado de serialização/deserialização

#OBS: O módulo Pickle não é seguro contra dados maliciosos (malware) e não deve ser usado para deserializar dados de fontes desconhecidas.


"""

import pickle


class Animal:
    def __init__(self, nome) -> None:
        self.__nome = nome

    @property
    def nome(self) -> str:
        return self.__nome

    def comer(self) -> str:
        return f"Animal: {self.__nome} está comendo"


class Gato(Animal):
    def __init__(self, nome) -> None:
        super().__init__(nome)

    def mia(self) -> str:
        return f"Gato: {self.nome} está miando"


class Cachorro(Animal):
    def __init__(self, nome) -> None:
        super().__init__(nome)

    def late(self) -> str:
        return f"Cachorro: {self.nome} está latindo"


felix = Gato("Felix")
pluto = Cachorro("Pluto")

with open("animais.pickle", "wb") as file:
    pickle.dump((felix, pluto), file)


# Fazer a leitura do arquivo pickle

with open("animais.pickle", "rb") as file:
    gato, cachorro = pickle.load(file)
    print(f"O gato chama-se {gato.nome}")
    gato.mia()
    print(f"O tipo do gato é {type(gato)}")

    print(f"O cachorro chama-se {cachorro.nome}")
    cachorro.late()
    print(f"O tipo do cachorro é {type(cachorro)}")
