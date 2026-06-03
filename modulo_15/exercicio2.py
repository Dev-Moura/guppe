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


# 2 - exercicio
class Agenda:

    def __init__(self):
        self.__contatos: list[Pessoa] = []


    @property
    def contatos(self) -> list[Pessoa]:
        return self.__contatos


    def armazenar_contato(self, contato: Pessoa) -> None:
        self.contatos.append(contato)


    def remover_contato(self, contato: Pessoa) -> None:
        self.contatos.remove(contato)

    
    def busca_contato(self, nome: str) -> None:
        for i, contato in enumerate(self.contatos):
            if contato.nome == nome:
                print(f'O contato {nome} esta na posição {i}')


    def imprimir_agenda(self) -> None:
        for c in self.contatos:
            c.imprimir()


    def imprimir_contato(self, i: int) -> None:
        self.contatos[i].imprimir()

    

if __name__ == '__main__':

    c1: Pessoa = Pessoa("Michael", date(2000, 6, 5), 'michael@email.com\n')
    c2: Pessoa = Pessoa("Angelina Jolie", date(1984, 3, 6), 'angelinajolie@email.com\n')
    c3: Pessoa = Pessoa("Ray Sychev", date(1981, 8, 18), 'raySychev@email.com\n ')

    agenda: Agenda = Agenda()

    agenda.armazenar_contato(c1)

    agenda.armazenar_contato(c2)

    agenda.armazenar_contato(c3)

    agenda.imprimir_agenda()

    agenda.busca_contato('Ray Sychev')

    agenda.imprimir_contato(2)

    agenda.remover_contato(c3)

    agenda.imprimir_agenda()
