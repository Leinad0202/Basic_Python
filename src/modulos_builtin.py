"""
Trabalhando com Módulos Builtin (módulo integrados, que já vem instalados no Python)
_________________________
|Python| Módulos builtin|
-------------------------

# Utilizando alias (apelidos) para módulos/funções
import random as rdm

print(rdm.random())


# Podmeos importar todas as funções de um módulo utilizando o *

from random import *
# import random

print(random)


# Importanto todo o módulo

import random

print(random.random())


# Utilizando alias (apelidos) para módulos/funções

from random import randint as rdi

print(rdi(5, 89))

"""

# Costumamos a utilizar ruple para colocar múltiplos imports de um mesmo módulo
from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())

print(randint(3, 7))

lista = ['geek', 'university', 'python']
shuffle(lista)
print(lista)

print(choice('University'))
