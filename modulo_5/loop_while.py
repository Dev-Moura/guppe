"""
Docstring for modulo_6.loop_while

Loop While

Forma geral

while expreesão_booleana:
    //execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira.

Expressão booleana é toda expressão onde o resultado é true or false.

Exemplo:

num = 5

num < 5 = false

C ou Java

while(expressão) {
//execução
}

do while (C ou Java)

do {
    //execução
}while(expressão);
"""

# Exemplo 1
num = 1 

while num < 10:
    print(num)
    num = num + 1
    
# OBS: Em um loop while, é importante que cuidemos do critério de parada.

# Exemplo 2

resposta = ''

while resposta != 'sim'.lower():
    resposta = input("Já acabou Jéssica? ")
