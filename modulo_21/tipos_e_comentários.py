import math


def circunferencia(raio):
    # type: (float) -> float
    return 2 * math.pi * raio


def cabecalho(texto, alinhamento=True) -> str:
    # type: (str, bool) -> str

    if alinhamento:
        return texto.center(80)
    else:
        return texto.ljust(80)


# método esquesito que funciona
def cabecalho2(
    texto,  # type: str
    alinhamento=True,  # type: bool
):  # type: (...) -> str

    if alinhamento:
        return texto.center(80)
    else:
        return texto.ljust(80)


cabecalho2(texto="42", alinhamento=False)
