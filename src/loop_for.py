"""
Looop for

Loop -> Estrutura de repetição
for  -> Uma dessas estruturas

C ou Java

for(int i = 0; i < 10; i++){
    //execução do loop
}

Python

for item in interavel:
    //execução do loop




Uilizamos loops para iterar sobre sequèncias ou sobre valores iteraveis

Exemplos de iteraveis:
- String
    nome = 'Geek University'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1,10)

# Exemplo de for 1 (Iterando uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)

range(valor_inicial, valor_final)

OBS: O valor final não é inclusive.
1
2
3
4
5
6
7
8
9
10 - não

for numero in range(1, 10):
    print(numero)

Enumerate:

((0, 'G'), (1, 'E'), (2, 'E'), (3, 'K'), (4, ' '), (5, 'U') ...)

for indice, letra in enumerate(nome):
    print(nome[indice])

for _, letra in enumerate(nome):
    print(letra)

OBS: Quando não precisamos de um valor, podemos descarta-lo utilizando um underline (_)

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em uma lista

for valor in enumerate(nome):
    print(valor)

qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

nome = 'Geek University'
for letra in nome:
    print(letra, end=' ')
    
"""





