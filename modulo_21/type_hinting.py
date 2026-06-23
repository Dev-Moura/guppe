"""
Type hinting

implementado na pep 484 e versão do python 3.5
"""


def cumprimentar(nome: str) -> str:
    return f"Olá, {nome}"


resultado = cumprimentar("Guilherme")
print(resultado)


def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f"{texto.title()}".center(50, "#")


print(cabecalho("Guilherme"))

print(cabecalho("Guilherme", alinhamento=False))
