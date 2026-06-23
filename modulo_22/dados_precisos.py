"""
- Literal type
- Union
- Final
- typed dictionares
- protocols
"""

"""
# Literal type

from typing import Literal


def pegar_status(user: str) -> Literal["online", "offline", "away"]:
    pass


def calcular(operacao: Literal["+", "-"], a: int, b: int) -> None:
    if operacao == "+":
        print(f"{a} + {b} = {a + b}")
    elif operacao == "-":
        print(f"{a} - {b} = {a - b}")
    else:
        raise ValueError(f"Operação inválida: {operacao!r}")


calcular("+", 6, 4)
calcular("-", 10, 4)
calcular("*", 6, 4)


# Union

from typing import Union


def soma(a: int, b: int) -> Union[str, int]:
    r: int = a + b

    if r > 50:
        return "Resultado {r} é muito alto"
    else:
        return r


from typing import Final

NOME: Final = "geek"

print(NOME)

NOME = "University"  # error

print(NOME)


@final  # Não deixa sobrescrever métodos
class Pessoa:
    pass


class Estudante:
    pass

    @final
    def estudar(self) -> None:
        print("Estou estudando...")


class Estagiario(Estudante):
    pass

    def estudar(self) -> None:
        print("Estudando e estagiando...")


# typed dictionaries

from typing import TypedDict


class CursoPython(TypedDict):
    versao: str
    atualizacao: float


print(geek := CursoPython(versao="3.8.5", atualizacao=2020))
"""
from typing import Protocol


class EstudanteProtocol(Protocol):
    number: str


def pagar(valor: EstudanteProtocol) -> str:
    return f"Pagando a {valor.number}"


class Mensalidade:
    number = "Mensalidade"


M1 = Mensalidade()

print(pagar(M1))
