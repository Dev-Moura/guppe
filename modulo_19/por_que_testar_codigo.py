"""
Testes

Por que testar código?
    - reduzir bugs
    - Testes garantem que novos recursos da sua aplicação funcionem como esperado
    - Testes ajudam a identificar problemas antes que eles se tornem problemas reais
    - Testes são uma forma de documentação para o seu código
    - Testes garantem que suas alterações não introduzam novos bugs

TDD - Test Driven Development (Desenvolvimento Orientado a Testes)

Com TDD é utilizado estágio de desenvolvimento
    - Você escreve os testes antes de implementar o código
    - Então você implementa o código para passar nos testes
    - Então refatora o código
    - Uma vez que os testes passam, o recurso é considerado completo

Estes estágios do TDD São quase como um mantra que os desenvolvedores segue, conhecidos como:
    - Red;
    - Green;
    - Refactor;

"""


class Gato:
    def __init__(self, nome):
        self.__nome = nome

    def miar(self):
        print(f"{self.__nome} está miando...")


felix = Gato("Felix")

felix.miar()

print(felix.nome)
