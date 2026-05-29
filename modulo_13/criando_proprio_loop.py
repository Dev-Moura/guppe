"""
Criando sua propria versao de loop


"""

for num in [1, 2, 3, 4, 5]:
    print(num)

for letra in 'geek university':
    print(letra)

iter([1, 2, 3, 4, 5])

iter('geek university')

def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

meu_for('geek university')

numeros = [1, 2, 3, 4, 5]

meu_for(numeros)