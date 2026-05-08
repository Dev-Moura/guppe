"""
modulos customizados

Como módulos Python nada mais são do que arquivos Python, então TODOS os arquivos que criamos
neste curso são módulos Python prontos para serem utilizados.

# Importando uma função específica do nosso módulo
from modulo_7.funcoes_com_parametro import soma_impares
"""
# Importando todo o módulo
import modulo_7.funcoes_com_parametro as fcp

# Estamos acessando e imprimindo uma variável contida no módulo
print(fcp.lista)
print(fcp.tupla)
print(fcp.soma_impares([1, 2, 3, 4, 5, 6, 7, 8, 9]))

from modulo_9.map import cidades, c_para_f

print(list(map(c_para_f, cidades)))