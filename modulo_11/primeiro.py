def funcao1():
    print('Geek University - primeiro.py')


if __name__ == '__main__':
    funcao1()
    print("primeiro.py está sendo executado diretamente")
else:
    print(f"O módulo primeiro.py foi importado, {__name__}")
