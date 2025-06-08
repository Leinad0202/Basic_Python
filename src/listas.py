"""
Listas (List)

Listas em Python funcional como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINÃMICO e também de podermos colocar QUALQUER tipo de dado.

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo;
    ou seja, nestas linguagens se você criar um array do tipo ont e com tamanho 5, este array
    será SEMPRE do tipo inteiro e podera ser SEMPRE no máximo 5 valores.

Já em python:

- Dinâmico: Não possui tamanho fixo; Ou seja, podemos criar a lista e semplesmente ir adicionando elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo; Ou seja, podemos colocar qualque yipo de dado;

As listas em Python são representados por colchetes: []

type([])

lista1 = [1, 99, 4, 27, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's' 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')


# Podemos facilmente checar se determinado valor está contido na lista
num = 7
if num in lista4:
    print(f'Encontrei o {num}')
else:
    print(f'não encontrei o {num}')

# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementos a listas

Para adicionar elementos em listas, utilizamos a função append

print(lista1)
lista1.append(42)
print(lista1)

# OBS: Com append, nós só conseguimos adicionar 1 elemento por vez
# lista1.append(12, 34, 56) # Erro

lista1.append([8, 3, 1])
print(lista1)

if [8, 3, 1] in lista1: # Coloca a lista como elemento unico
    print('Encontrei a lista')
else:
    print('não encontrei a lista')

lista1.extend([123, 44, 67]) # Coloca cada elemento da lista como valor adicional
print(lista1)

# podemos inserir um novo elemento na lista informando a posição do índice
# OBS: Isso não substitui o valor inicial. O mesmo será deslocado para a direita da lista.

lista1.insert(2, 'Novo Valor')
print(lista1)

#Podemos facilmente juntar duas listas

lista6 = lista1 + lista2
# lista1.extend(lista2)
print(lista1)

#Podemos facilmente inverter uma lista

# Forma 1
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

# Forma 2
print(lista1[::-1])
print(lista2[::-1])

# Copiar uma lista
lista6 = lista2.copy()
print(lista6)

# Podemos contar quantos elementos existem dentro de uma lista
print(len(lista5))


# Podemos remover facilmente o último elemento de uma lista
# OBS: O pop não somente remove o ultimo elemento mas também o retorna
print(lista5)
lista5.pop()
print(lista5)

#Podemos remover um elemento pelo índice
# OBS: Os elementos do indice á direita, foram deslocados  para a esquerda
# OBS: Se não houver elemento no indice informado, teremos o index erro
lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos(Zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Podemos facilmente converter uma string para uma lista

# Exemplo 1

curso = 'Programação em Python Essencial'
print(curso)
curso = curso.split()
print(curso)

# OBS: Por padrão o split separa os elementos por espaço

# Exemplo 2
curso = 'programação,em,Python,Essencial'
print(curso)
curso = curso.split(',')
print(curso)


# Convertendo uma lista em uma String

lista6 = ['Programação', 'em', 'Python', 'Essencial']
print(lista6)

# Abaixo estamos falando: pega a lista6, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

# Abaixo estamos falando: Pega a lista6, pega a lista6 e coloca o cifrão depois de cada elemento e transforma em string
curso = '$'.join(lista6)
print(curso)


#Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados
lista6 = [1, 2, 34, True, 'Geek', 'd', [1,2,3], 43445435636636]
print(lista6)
print(type(lista6))

# Iterando sobre listas

# Exemplo 1 - Utilizando for

soma = 0
for elemento in lista4:
    print(elemento)
    soma = soma + elemento
print(soma)


# Exemplo 2 = Utilizando while

carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair:")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)


# Utilizando variáveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)


# Fazemos acesso aos elementos de forma indexada

#           0         1         2       3
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0]) # verde
print(cores[1]) # amarelo
print(cores[2]) # azul
print(cores[3]) # branco

# Fazer acesso aos elementos de forma indexada inversa
# Para entender melhor o indice negativo pense na lista como um circulo, onde
# o final de um elemento rsta ligado ao inicio da lista

print(cores[-1]) # branco
print(cores[-2]) # azul
print(cores[-3]) # amarelo
print(cores[-4]) # verde
# print(cores[-5]) # Erro, pois não existe indice -5

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1


# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

# Listas aceitam valores repetidos

lista = []

lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)

print(lista)


# Outros métodos não tão importantes mas támbem úteis

# Encontrar o índice de um elemento na lista

numeros = [5, 6, 7, 5, 8, 9, 10]

# Em qual índice está o valor 6?
print(numeros.index(6))

# Em qual índice da lista está o valor 9?
print(numeros.index(9))

# print (numero.index(9)) # gera ValueError

# OBS: Caso não tenha este elemento na lista, será apresentado erro ValueError

# Retorna o índice do primeiro elemento encontrado
print(numeros.index(5))

# Podemos fazer busca dentro de um range, ou seja, qual índice começar a buscar
print(numeros.index(5, 1)) # Buscando a partit do índice 1
print(numeros.index(5, 2)) # Buscando a partit do índice 1
print(numeros.index(5, 3)) # Buscando a partit do índice 1
#print(numeros.index(5, 4)) # Buscando a partit do índice 1
# OBS: Caso não tenha este elemento na lista, será apresentado erro ValueError

# Podemos fazer busca dentro de um range, inicio/fim
print(numeros.index(8, 3, 6)) # Buscar o índice de valor 8, entre o indice 3 e 6


# Revisão de slicing

# lista [inicio:fim:passo]
# range (inicio:fim:passo)

#Trabalhando com slice de lista com o parâmetro 'inicio'

lista = [1, 2, 3, 4]

print(lista[1:]) # Iniciando no índice 1 e pegando todos elementos restantes

# Trabalhando com slice de lista com o parâmetro 'fim'

print(lista[:2]) # começa em 0, pega até o índice 2 - 1
print(lista[:4]) # começa em 0, pega até o índice 4 - 1
print(lista[1:3]) # começa em 1, pega até o índice 3 - 1

# Trabalhando com slice de lista com o parâmetro 'passo'

print(lista[1::2]) # Começa em 1, vai até o final, de 2 em 2
print(lista[::2]) # começa em 0, vai até o final, de 2 em 2


#invertendo valores em uma lista

nomes = ['Geek', 'University']

nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

nomes = ['Geek', 'University']

nomes.reverse()
print(nomes)


# Soma*, Valor Maxímo*, Valor Minímo*, Tamanho

# * Se os valores forem todos inteiros ou reais

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista)) #soma
print(max(lista)) #máximo valor
print(min(lista)) #mínimo valor
print(len(lista)) #tamanho da lista


#Tranformar uma lista em tuplas

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))


#Desempacotamento de listas

lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

# OBS: Se tivermos um número diferente de elementos na lista para receber os dados, teremos ValueError


# Copiando uma lista para outra (Shallow copy e Deep Copy)

# Forma 1 Deep Copy

lista = [1, 2, 3]
print(lista)

nova = lista.copy()

print(nova)

nova.append(4)

print(lista)
print(nova)

#Veja que ao utilizarmos listas.copy() copiamos os dados da lista para uma nova listam, mas elas
# ficaram totalmente indenpendentes, ou seja, modificando uma lista, não afeta a outra, Isso em python
# é chamado de Deep Copy (cópia profunda)


# Forma 2 - Shallow Copy

lista = [1, 2, 3]
print(lista)

nova = lista # cópia

print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista mas após realizar
# modificação em uma das listas, essa modificação se refletiu em ambas as listas
# Isso em Python é chamado de Shallow Copy

"""