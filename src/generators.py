"""
Generators

Em aulas anteriores nós estudamos:
 - List Comprhension;
 - Dictionary Comprehension;
 - Set Comprehension;

Não vimos:
 - Tuple Comprehension.... porque elas se chamam Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any[nome[0] == 'C' for nome in nomes])


# Poderíamos ter feito utilizando Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any(nome[0] == 'C' for nome in nomes))

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print((res))


# Qual é a utilidade de getsizeof()? -> Retorna a quantidade de bytes em memória do elemento passado como parâmetro
from sys import  getsizeof

# Mostra quantos bytes a string 'Geek' está ocupando em memória. Quando maior a string, mais espaço ocupa

print(getsizeof('Geek'))

print(getsizeof('University'))

print(getsizeof(9))

print(getsizeof(91))

print(getsizeof(34563632562624363))

print(getsizeof(True))


from sys import  getsizeof

# Gerando uma lista de números com List Comprehension
list_comp = getsizeof([x * 10 for x in range(10000)])

# Gerando uma lista de números com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(10000)})

# Gerando uma lista de números com Dictionary Comprehension
dic_comp = getsizeof({x: x * 10 for x in range(10000)})

# Gerando uma lista de números com Generator
gen = getsizeof((x * 10 for x in range(10000)))

print(f'List Comprehension {list_comp}')

print(f'Set Comprehension {set_comp}')

print(f'Dictionary Comprehension {dic_comp}')

print(f'Generator: {gen}')



"""

# Eu posso iterar no Generator Expression? Sim!

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)