"""
Escrevendo um iterador customizado

for jabuticaba in range(11):
    print(jabuticaba)



"""
from poetry.console.commands import self



class Contator:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero

        raise StopIteration

con = Contator(1, 61)

for i in con:
    print(i)