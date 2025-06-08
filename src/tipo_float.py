"""
tipo float

tipo real, decimal

casas decimais

OBS: O separados de casa decimais na programação é o ponto e não a virgula.
"""

# Errado
valor = 1, 44
print (valor)
print(type(valor))

#Certo
valor = 1.44
print(valor)
print(type(valor))

#É possivel fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

#podemos converter um float para um int
'''
OBS:Ao converter valores float para int, nós perdemos precisão
'''
res = int(valor)
print(res)
print(type(res))

#podemos trabalhar com numeros complexos

variavel = 5j