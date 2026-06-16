"""
Escrevendo em arquivos CSV


reader() (leitor), writer() (escritor)

writerow() -> Escreve uma linha

"""

# writer() -> Gera um objeto para que possamos escrever em um arquivo CSV. Utilizamos o método
# writerow() para escrever uma linha no arquivo. Este método recebe uma lista.

from csv import writer

with open("filmes.csv", "w") as arq:
    escritor_csv = writer(arq)
    filme = None
    escritor_csv.writerow(["Título", "Gênero", "Duração"])
    while filme != "sair":
        filme = input("Informe o nome do filme")
        if filme != "sair":
            genero = input("Informe o gênero: ")
            duracao = input("Informe a duração (em minutos): ")
            escritor_csv.writerow([filme, genero, duracao])

# DictWriter()

from csv import DictWriter

with open("filmes_dict.csv", "w") as arq:
    # cabecalho = ['Título', 'Gênero', 'Duração'] podemos passar uma lista ou dict para o fieldnames
    escritor_dict = DictWriter(arq, fieldnames=["Título", "Gênero", "Duração"])
    escritor_dict.writeheader()
    filme = None
    while filme != "sair":
        filme = input("Informe o nome do filme")
        if filme != "sair":
            genero = input("Informe o gênero: ")
            duracao = input("Informe a duração (em minutos): ")
            escritor_dict.writerow(
                {"Título": filme, "Gênero": genero, "Duração": duracao}
            )
