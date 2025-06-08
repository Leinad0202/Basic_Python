"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas.

Existem basicamente duas diferenças básicas:

1 - As tuplas são representadas por parênteses ()

2 - As tuplas são imutáveis: Isso significa que ao criar uma tupla ela não muda. Toda
operação em uma tupla gera uma nova tupla.

# CUIDADO 1: As tuplas são representadas por ()

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)

print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)

print(type(tupla2))

# CUIDADO 2: Tuplas com 1 elemento

tupla3 = (4) # Isso não é uma tupla!
print(tupla3)

print(type(tupla3))

tupla4 = (4,) # Isso é uma tupla!
print(tupla4)

print(type(tupla4))

tupla5 = 4, # Isso é uma tupla!
print(tupla5)

print(type(tupla5))

# CONCLUSÃO: Podemos concluir que tuplas são definidas pela virgula e não pelo uso de parênteses

(4) - não é tupla
(4,) - é tupla
4, - é tupla


#Podemos gerar uma tupla dinamicamente com range ()inicio,fim,passos)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))


#desempacotamento de tupla

tupla = ('geek university', 'programação em Python: Essencial')

escola, curso = tupla

print(escola)
print(curso)

# OBS: Gera erro (ErrorValue) se colocarmos um número diferente de elementos para desenpacotar.


#Métodos para adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutaveis


# Soma*, Valor Maxímo*, Valor Minimo* e tamanho

# * Se os valores forem todos inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6,)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))


# Concatenação de tuplas

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print( tupla1 + tupla2) # Tuplas são imutáveis

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2
print(tupla3)
print(tupla1)
print(tupla2)

tupla1 = tupla1 + tupla2 # Tuplas são ímutaveis, mas podemos sobrescrever seus valores
print(tupla1)


# Verificar se determinado elemento está contido na tupla

tupla = (1, 2, 3)

print(3 in tupla)



# Iterando sobre uma tupla

tupla = (1, 2, 3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)


# Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')

print(tupla.count('c'))

escola = tuple('Geek University')
print(escola)

print(escola.count('e'))


# Dicas na utilização de tuplas

# Devemos utilizar tuplas Sempre que não precisamos modificar os dados contidos em uma coleção

# Exemplo 1

meses = ('Janeiro', 'Fevereiro', 'março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

# Slicing

# tupla[inicio:fim:passo]

print(meses[5:9])

print(meses)

# O acesso de elementos de uma yupla é semelhante a de uma lista

print(meses[5])

# Iterar com while

i = 0

while i < len(meses):
    print(meses[i])
    i = i + 1


# Verificamos em qual índice um elemento está na tupla

print(meses.index('Junho'))

# OBS: Caso o elemento não exista, será gerado ValueError


# Por quê utilizar tuplas?

# - tuplas são mais rapido do que listas.
# - Tuplas deixam seu codigo mais seguro*.

# - Isso porque trabalhar com elementos imutaveis traz segurança para seu codigo.


# Copiando uma tupla para outra

tupla = (1, 2, 3)
print(tupla)

nova = tupla # na tupla não temos o problema de shallow copy

print(nova)
print(tupla)

outra = (4, 5, 6)

nova = nova + outra

print(nova)
print(tupla)

"""
