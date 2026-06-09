"""
POO - Herança (Inheritance)

A ideia de herança é a de reaproveitar código. Tambḿe extender nossas classes.

OBS: Com a Herança, a partir de uma classe existente, nós extendemos outra classe
que passa a herdar atributos e métodos da classe herdada.

Cliente
    - nome;
    - sobrenome;
    - cpf;
    - renda;

Funcionário
    - nome;
    - sobrenome;
    - cpf;
    - matricula;

Pergunta: Existe alguma entidade genérica o suficiente para encapsular os atributos e métodos comuns a entidades Cliente e Funcionário?


OBS: Quando uma classe herda de outra classe, ela herda todos os atributos e métodos da classe herdada.

Quando uma classe herda de outra classe, a classe herdada é conhecida por:
    [Pessoa]
    - Super Classe;
    - Classe Base;
    - Classe Pai;
    - Classe Mãe;
    - Classe Genérica;

Quando uma classe herda de outra classe, a classe herdade, é conhecida por:
    - Sub Classe;
    - Classe Filha;
    - Classe Específica;
    - Classe Derivada;
    - Classe Hija;
    - Classe Filho;

Sobrescrita de método, ocorre quando reescrevemos um método presente na super classe em uma sub classe.
"""


class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"


class Cliente(Pessoa):
    """Cliente herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionário herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    # Sobrescrita de Métodos (Overriding)
    def nome_completo(self):
        print(super().nome_completo())
        print(self._Pessoa__cpf)
        return f"Funcionário: {self.__matricula} Nome:{self._Pessoa__nome}"


cliente1 = Cliente("Angelina", "Jolie", "123.456.789-00", 5000)
funcionario1 = Funcionario("Felicity", "Jones", "987.654.321-00", 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
