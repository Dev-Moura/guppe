"""
Trabalhando com deltas de data e hora

data_inicial = dd/mm/yyyy 13:55:34.9939329
data_inicial = dd/mm/yyyy 13:34:23.9939329

delta = data_final - data_inicial
"""

import datetime

# Temos a data de hoje
data_hoje = datetime.datetime.now()

# Data para ocorrer um determinado evento no futuro
aniversario = datetime.datetime(2019, 3, 3, 0)

tempo_para_evento = aniversario - data_hoje

print(type(tempo_para_evento))

print(repr(tempo_para_evento))

print(tempo_para_evento.days)

print(f"Faltam {tempo_para_evento.days} dias, {tempo_para_evento / 60} horas...")

data_da_compra = datetime.datetime.now()

print(data_da_compra)

regra_boleto = datetime.timedelta(days=3)

print(regra_boleto)

data_de_vencimento = data_da_compra + regra_boleto

print(data_de_vencimento)
