"""
JSON e Pickle

JSON -> JavaScript Object Notation

API -> Application Programming Interface
"""

import json
import re

import jsonpickle

ret = json.dumps(["Produto", {"Playstation 4": ("2TB", "Novo", "4K", 2340)}])
print(type(ret))
print(ret)


class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def raca(self) -> str:
        return self.__raca


felix = Gato("Felix", "Siamese")


with open("felix.json", "w") as file:
    ret = jsonpickle.encode(felix)
    file.write(str(ret))


with open("felix.json", "w") as file:
    conteudo = file.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)
