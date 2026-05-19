import primeiro


def funcao2():
    primeiro.funcao1()

if __name__ == "__main__":
    funcao2()
    print("Segundo.py está sendo executado dir  etamente")
else:
    print(f"O módulo segundo.py foi importado, {__name__}")