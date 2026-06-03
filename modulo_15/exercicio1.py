# 1 Exercicio
from datetime import date

class Pessoa:
    def __init__(self, nome: str, data_nascimento: date, email: str):
        self.__nome: str = nome
        self.__data_nascimento: date = data_nascimento
        self.__email: str  = email

    def imprimir(self) -> None:
        print(f"Nome: {self.nome}")
        print(f"Data Nascimento: {self.data_nascimento.strftime('%d/%m/%Y')}")
        print(f"E-mail: {self.email}") 

    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    @property
    def data_nascimento(self):
        return self.__data_nascimento
    
    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: date) -> None:
        self.__data_nascimento = data_nascimento
    
    @property
    def email(self) -> str:
        return self.__email
    
    @email.setter
    def email(self, email: str) -> None:
        self.__email = email


if __name__ == '__main__':
    p: Pessoa = Pessoa('Michael de Souza', date(2000, 6, 5), 'michael.moura@gmail.com')
    p.imprimir()
