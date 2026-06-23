import random

NAIPES = "♠ ♡ ♢ ♣".split()
CARTAS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

CARTA = tuple[str, str]
BARALHO = list[CARTA]


def criar_baralho(aleatorio: bool = False) -> BARALHO:
    """Criar um baralho de cartas."""
    baralho: BARALHO = [(n, c) for c in CARTAS for n in NAIPES]
    if aleatorio:
        random.shuffle(baralho)
    return baralho


def distribuir_cartas(
    baralho: BARALHO,
) -> tuple[BARALHO, ...]:
    """Gerencia a mão de cartas de acordo com o baralho gerado."""
    return (baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4])


def jogar() -> None:
    """Inicia o jogo distribuindo cartas e gerenciando as mãos dos jogadores."""
    cartas: BARALHO = criar_baralho(aleatorio=True)
    jogadores = "P1 P2 P3 P4".split()
    maos = {j: m for j, m in zip(jogadores, distribuir_cartas(cartas))}

    for jogador, cartas in maos.items():
        carta: str = " ".join(f"{j}{c}" for (j, c) in cartas)
        print(f"{jogador}: {carta}")


if __name__ == "__main__":
    jogar()
