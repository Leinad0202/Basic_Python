"""

Ranges

- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loop for.

Ranges são utilizados para gerar sequèncias numéricas, não de forma aleatória,
mas sim de maneira especifica.
Formas gerais:

# Forma 1

range(valor_de_parada)

OBS: valor_de_parada não inclusive (inicio padrão 0, e passo de 1 em 1)

#Forma 1
for num in range(11):
    print(num)

#Forma 2

range(valor_de_inicio, valor_de_parada)

OBS: valor_de_parada não inclusive (inicio especificado pelo usuario, e passo de 1 em 1)

#Exemplo forma 2

for num in range(4, 11):
    print(num)

#Forma 3

range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada_ não inclusive (inicio especificado pelo usuário, e passo especificado pelo usuario)

# Exemplo de forma 3

for num in range(5, 55, 5):
    print(num)

Forma 4 (Inversa)

range(valor_de_final, valor_de_parada, passo)

OBS: valor_de_parada não inclusive (início especificado pelo usuário, e passo especificado pelo usuário)

# Exemplo forma 4
for num in range(10, -1, -1):
    print(num)



"""






