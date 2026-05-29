"""
Preservando metadas com wraps

Metadados -> sao dados intrisecos em arquivos

wraps -> sao funçoes que envolvem elementos com diversos finalidades.

"""

# Problema

def ver_log(funcao):
    def logar(*args, **kwargs):
        """Eu sou uma funçao (logar) dentro de outra"""
        print(f'Voce esta chamando {funcao.__name__}')
        print(f'Aqui esta documentacao {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    """Soma dois numeros."""
    return a + b

print(soma.__name__)
print(soma.__doc__)


# resoluçao do problema

from functools import wraps

def resolucao_ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma funçao (logar) dentro de outra"""
        print(f'Voce esta chamando {funcao.__name__}')
        print(f'Aqui esta documentacao {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@resolucao_ver_log
def soma(a, b):
    """Soma dois numeros."""
    return a + b

print(soma.__name__) # soma
print(soma.__doc__) # soma dois numeros