"""
POO - Classes

Em POO, Classes nada mais sao do que modelos dos objetos do mundo real sendo representados
computacionalmente.

Imagine criar um sistema para automatizar o controle das lampadas da sua casa.

Classes podem conter:
    - Atributos -> Representam as caracteristicas do objeto. Ou seja, pelos atributos conseguimos
    representar computacionalmento os estados de um objeto. No caso da lampada, possivelmente
    iriamos querer saber se a lampada e 110 ou 220 volts, se ela e branca, amarela, vermelha ou
    outra cor, qual e a luminosidade dela e etc.

    - Metodos (funçoes) -> que representam os comportamentos do objeto. Ou seja, as acoes que este
    objeto pode realizar no seu sistema. No caso da lampad, por exemplo, um comportamento comum
    que muito provavelmente iriamos querer representar no nosso sistema e o de ligar e desligar
    a mesma.

Em python, para definir uma classe utilizamos a palavra reservada class.

OBS: Utilizamos a palavra 'pass' em Python quando temos um bloc de codigo que ainda nao esta implementado.

OBS: Quando nomeamos nossas classes em Python utilizamos por convençao o nome com inicial
em maiusculo. ou seja CamelCase.

Dica Geek: Em computaçao nao utilizamos: acentuaçao, caracteres especiais, espaço ou similares
para nomes de classes atributos, metodos, arquivos, diretorios e etc.

OBS: Quando estamos planejando um software e definimos quais classes teremos que ter no sistemas, chamamos estes
objetos que serao mapeados para classes de entidade.
"""
class Lampanda:
    pass

class contaCorrente:
    pass

class Produto:
    pass

class Usuario:
    pass

lamp = Lampanda()
print(type(lamp))


valor = int('42')

print(help(int))