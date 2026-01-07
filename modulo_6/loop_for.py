"""
Loop for

Loop -> Estrutura de repetição
For -> Uma dessas estruturas

C ou Java

for(int i = 0; i < 10; i++ ) {
    //execução do loop
}

Python

for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
- String
    nome = 'Geek University'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1, 10)

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

# Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra)



# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)


# Exemplo de for 3 (Iterando sobre um range)
# range(valor_inicial, valor_final)
# OBS: o range começa do 0
for numero in range(1, 10):
    print(numero)

    
enumerate

for i, v in enumerate(nome):
    print(nome[i])
    


OBS: Quando não precisamos de um valor, podemos descartá-lo utilizando o underline
for _, l in enumerate(nome):
    print(l)


    
for valor in enumerate(nome):
    print(valor[0])
   
    """


nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # temos que transformar em uma lista



qtd = int(input("Quantas vezes esse loop deve rodar?"))
soma = 0


for n in range(1, qtd):
    print(f'Imprimindo{n}')


for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} vqlor: '))
    soma = soma + num
print(f'A soma é {soma}')