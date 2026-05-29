"""
Geradores

 - Geradores (Generators) sao iterators (iteradores):

 OBS: O contrario nao e verdadeiro. Ou seja, nem todo iterator e um generator.

 Outras Informaçoes:
    - Generators podem ser criadas com funçoes geradores;
    - funçoes geradoras utilizam a palavra reservada yield;
    - Generators podem ser criados com expressoes Geradoras;

    Diferença entre funçoes e generators functions (funçoes geradoras)

-------------------------------------------------------------------
/ funçoes                   /   Generator functions               /
-------------------------------------------------------------------
/ utilizam return           /   utilizam yield                    /
-------------------------------------------------------------------
/ retornar uma vez          / podem utilizar yield mutiplas vezes /
-------------------------------------------------------------------
/ Q executada retorna um valor /                                  /
-------------------------------------------------------------------


"""

# Exemplo Generator Function

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1

# OBS: um generator function nao e um generator. Ela gera um genenretor.

gen = conta_ate(10)

for G in gen:
    print(G)

# podemos transformar em listas

gen = conta_ate(10)

print(list(gen))