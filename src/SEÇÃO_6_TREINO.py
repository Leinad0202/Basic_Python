"""
1. Crie um programa que lê 6 valores inteiros, armazene em uma lista e em seguida mostre na tela os valores lidos

lista: list[int] = []

while len(lista) < 6:
    valor: int = int(input(f'Informe o valor {len(lista) + 1}/6: '))
    lista.append(valor)

for valor in lista:
    print(valor)

     2. Faça um programa que possua uma lista denominada A que armazene 6 números inteiros. O programa
deve executar os seguintes passos:
 a) Atribua os seguintes valores a essa lista: 1, 0, 5, -2, -5, 7.
 b) Armazene em uma variável inteira a soma entre os valores das posições A[0], A[1] e A[5] da lista e mostre
na tela esta soma.
 c) Modifique a lista na posição 5, atribuindo a esta posição o valor 100.
 d) Mostre na tela cada valor da lista A, um em cada linha

# A

a: list[int] = [1, 0, 5, -2, -5, 7]

# B

soma: int = a[0] + a[1] + a[5]
print(f'A soma dos valores é {soma}')

# C

a[5] = 100
print(a)

# D

for valor in a:
    print(valor)

3. Faça um programa que leia 10 valores, armazene-os em uma lista e apresente quantos valores pares ele
possui

"""

lista: list[int] = []

while len(lista) < 10:
    valor: int = int(input(f' Informe o valor {len(lista) + 1}/10: '))
    lista.append(valor)

print(f'sua lista é {lista}')

for valor in lista:
    if valor % 2 == 0:
        print(valor)