class CisneNegro:
    def __len__(
        self,
    ):
        return 42


livro = CisneNegro()
print(len(livro))


nome = "Geek University"
lista = [12, 32, 44, 68]
dicio = {"carlos": 12, "vanessa": 32, "joana": 44}


print(len(nome))
print(len(lista))
print(len(dicio))

# se determinado objeto anda como um pato, nada como um pato, parece com um pato, logo é um pato -> duck tipyng


idade = 43
peso = 81.4

print(len(idade))
