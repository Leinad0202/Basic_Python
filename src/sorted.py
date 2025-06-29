"""
Sorted

OBS: Não confunda, apesar do nome, com a função sort() que já estudamos em listas. O sort()
só funciona em listas.

Podemos utilizar o sorted() com qualquer iterável.

Como o próprio nome diz, sorted() serve para ordenar.

OBS: O sorted, SEMPRE retorna uma lista com os elementos do iterável ordenados

# Exemplo

numeros = [6, 1, 8, 2]
print(numeros)

print(sorted(numeros)) # Ordenar do menor para o maior

print(numeros)


numeros = [6, 1, 8, 2]
print(numeros)

print(sorted(numeros)
# Adicionando parâmetros ao sorted()

print(sorted(numeros, reverse=True)) # Ordena do maior para o menor


# Podemos utilizae o sorted() para coisas mais complexas

usuarios = [
    {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': 'carla', 'tweets': ['eu amo gatos']},
    {'username': 'jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': [], 'cor': 'amarelo'},
    {'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']},
    {'username': 'gal', 'tweets': [], 'cor': 'pretp', 'musica': 'rock'}
]

print(usuarios)

# Ordenando pelo username - Ordem alfabética
print(sorted(usuarios, key=lambda usuario: usuario['username']))

# Ordenando por numero de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets'])))


"""

# Último exemplo

musicas = [
    {'titulo': 'Thunderstruck', 'tocou': 3},
    {'titulo': 'Dead Skin Mask', 'tocou': 2},
    {'titulo': 'Back in Black', 'tocou': 4},
    {'titulo': 'Too old to rock´in roll, too young to die', 'tocou': 32}
]

# Ordena da menso tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica ['tocou']))

print(sorted(musicas, key=lambda musica: musica ['tocou'], reverse=True))
