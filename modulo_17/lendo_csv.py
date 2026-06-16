"""
Lendo arquivos CSV

CSV - Comma Separeted Values - Valores separados por vírgula

# Separador por vírgula

1, 2, 3, 4, 5, 6, 7, 8

# Separador por espaço

1 2 3 4 5 6 7 8


# Possível de se trabalhar, mas não é o ideal

with open("lutadores.csv") as arq:
    dados = arq.read()
    # print(type(dados))
    dados = dados.splitlines(",")[2:]
    print(dados)


A linguagem python possui duas dormas diferentes para ler dados em arquivos CSV:
    - reader -> Permite que iteremos sobre as linhas do arquivo CSV com listas;
    - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV com dicionários;


"""

# Reader

from csv import reader

with open("lutadores.csv") as arq:
    leitor_csv = reader(arq)
    next(leitor_csv)  # Pular o cabeçalho
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f"{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]} cm")

# DictReader

from csv import DictReader

with open("lutadores.csv") as arq:
    leitor_csv = DictReader(arq, delimiter=",")
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(
            f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (cm)']} cm"
        )
