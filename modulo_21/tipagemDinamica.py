idade = 27
print(type(idade))

idade = "Quarenta e dois"
print(type(idade))


if False:
    resultado = 1 + "geek"  # erro, problema de tipagem dinamica

else:
    resultado = 1 + 42

print(resultado)
# Erro estourou na execução
