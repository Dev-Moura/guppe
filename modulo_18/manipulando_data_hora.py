"""
Manipulando Data e Hora

Python tem um módulo built-in (integrado) para se trabalhar com data e hora.
chamado datetime


"""

import datetime

print(dir(datetime))

print(datetime.MAXYEAR)
print(datetime.MINYEAR)

print(datetime.datetime.now())  # 2026-06-16 10:11:59.502939 BR 16/06/2026

# datetime.datetime(year, month, day, hour, minute, second, microsecond)
print(repr(datetime.datetime.now()))

# replace() para fazer ajustes da data/hora

inicio = datetime.datetime.now()

print(inicio)

# Alterar o horário para 16 horas, 0 minuto, 0 segundo, 0 microsegundo
inicio = inicio.replace(year=2023, hour=16, minute=0, second=0, microsecond=0)

print(inicio)


evento = datetime.datetime(2027, 1, 1, 0)

print(type(evento))

print(type("31/12/2027"))

print(evento)


nascimento = input("Digite sua data de nascimento: (dd/mm/yyyy)")

print(nascimento)

nascimento = nascimento.split("/")

nascimento = datetime.datetime(
    int(nascimento[2]), int(nascimento[1]), int(nascimento[0])
)

print(nascimento)

print(type(nascimento))

# Acesssa indicidual dos elementos de data e hora

print(evento.year)
print(evento.month)
print(evento.day)
print(evento.hour)
print(evento.minute)
print(evento.second)
print(evento.microsecond)
