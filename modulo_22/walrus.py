"""
O operador Walrus permite fazer a tribuição e retorno de valor em uma única expressão

variavel := expressao




"""

# normalmene fazemos

nome = "Geek University"
print(nome)

# com o walrus fazemos

print(nome := "Geek University")

# python 3.7
cesta = []
fruta = input("Informe a fruta: ")
while fruta != "jaca":
    cesta.append(fruta)
    fruta = input("Informe a fruta: ")

print(cesta)


# python 3.8+
cesta = []
while (fruta := input("Informe a fruta: ")) != "jaca":
    cesta.append(fruta)
