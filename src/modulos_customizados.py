"""
Módulo Customizados

Como módulos Python nada mais são do que arquivos Python, então TODOS os arquivos que criamos
neste curso são módulos Python peontos para serem utilizados

# Importando uma função especifica do nosso módulo
from funcoes_com_parametro import  soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6, 7, 8, 9]))


# Importando todo o modulo (temos acesso a TODOS os elementos do módulo)
import  funcoes_com_parametro as fcp


# Estamos acessando e imprimindo ums variavel contida no módulo
print(fcp.lista)

"""

from map import cidades, c_para_f

print(list(map(c_para_f, cidades)))