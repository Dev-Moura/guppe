"""
Métodos de Data e Hora


"""

import datetime
from shlex import join
from timeit import timeit

# Com o now() podemos especificar o formato da data e hora
agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(agora)


hoje = datetime.date.today()
print(hoje)

manutencao = datetime.datetime.combine(
    (datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time()
)

print(manutencao)

# encontrar o dia da semana. Weekday()

# Os dias da semana do método weekday()  começa em 0 (segunda-feira) e termina em 6 (domingo)

print(manutencao.weekday())

aniversario = input("Qual é o seu aniversário? ")

aniversario = aniversario.split("/")

aniversario = datetime.datetime(
    year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0])
)

while aniversario != "sair":
    match aniversario.weekday():
        case 0:
            print("Você nasceu na Segunda-feira")
            break
        case 1:
            print("Você nasceu na Terça-feira")
            break
        case 2:
            print("Você nasceu na Quarta-feira")
            break
        case 3:
            print("Você nasceu na Quinta-feira")
            break
        case 4:
            print("Você nasceu na Sexta-feira")
            break
        case 5:
            print("Você nasceu no Sábado")
            break
        case 6:
            print("Você nasceu no Domingo")
            break


hoje = datetime.datetime.today()

print(hoje)

hoje_formatado = hoje.strftime("%d/%m/%Y")
print(hoje_formatado)

from textblob import TextBlob


def formatar(data):
    return (
        f"{data.day} de {TextBlob(str(data.month)).translate(to='pt')} de {data.year}"
    )


hoje = datetime.datetime.today()
print(formatar(hoje))

import timeit

# Marcando tempo de execução

# loop for
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=1000000)
print(tempo)


# list comprehension
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=1000000)
print(tempo)

# Map
tempo = timeit.timeit('"-".join(map(str, range(100)))', number=1000000)
print(tempo)
