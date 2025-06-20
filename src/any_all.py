"""
Any e All


all() -> Retorna True se todos os elementos do iteravel são verdadeiros ou ainda se o iteravel está vazio


# Exemplo all()

print(all([0, 1, 2 ,3 ,4])) # Todos os números são verdadeiros? False

print(all([1, 2 ,3 ,4])) # Todos os números são verdadeiros? True

print(all([])) # Todos os números são verdadeiros? True

print(all((1, 2 ,3 ,4))) # Todos os números são verdadeiros? True

print(all({1, 2 ,3 ,4})) # Todos os números são verdadeiros? True

print(all('Geek')) # Todos os números são verdadeiro? True

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina',]

print(all([nome[0] == 'C' for nome in nomes]))

print(all([letra in 'aeiou' for letra in 'eiof']))  # Isso dá False

# OBS: Um iterável vazio convertido em boolean é False, maso all() entende como True
# print(all([letra for letra in 'eio' if letra in 'aeiou']))

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 1]))

any() -> Retorna True se qualquer elemento de iterável for verdadeiro, Se o iterável estiver vazio, retorna False


"""

print([0, 1, 2, 3, 4]) # True

print(any([0, False, [], (), {}])) # False

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina',]

print(any([nome[0] == 'C' for nome in nomes]))

print(any([num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0]))