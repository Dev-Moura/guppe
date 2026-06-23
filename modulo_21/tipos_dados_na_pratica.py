"""
nomes: list = ["Guilherme", "Maria", "João"]

versoes: tuple = (3, 4, 7)

opcoes: dict = {"ar": True, "Banco_couro": True}

valores: set = {3, 4, 7, 9}


# python profissional

nomes: list[str] = ["Guilherme", "Maria", "João"]

versoes: tuple[int, ...] = (3, 4, 7)

opcoes: dict[str, bool] = {"ar": True, "Banco_couro": True}

valores: set[int] = {3, 4, 7, 9}

"""

import random

NAIPES = "♠ ♡ ♢ ♣".split()
CARTAS = "2 3 4 5 6 7 8 9 10 J Q K A".split()


def criar_baralho(aleatorio=False):
    """Criar um baralho de cartas."""
    baralho = [(n, c) for c in CARTAS for n in NAIPES]
    if aleatorio:
        random.shuffle(baralho)
    return baralho


def distribuir_cartas(baralho):
    """Gerencia a mão de cartas de acordo com o baralho gerado."""
    return (baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4])


def jogar():
    """Inicia o jogo distribuindo cartas e gerenciando as mãos dos jogadores."""
    cartas = criar_baralho(aleatorio=True)
    jogadores = "P1 P2 P3 P4".split()
    maos = {j: m for j, m in zip(jogadores, distribuir_cartas(cartas))}

    for jogador, cartas in maos.items():
        cartas = " ".join(f"{j}{c}" for (j, c) in cartas)
        print(f"{jogador}: {cartas}")


if __name__ == "__main__":
    jogar()
