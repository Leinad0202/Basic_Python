"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.


# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)

print(f'Média: {media}')

#OBS: Assim como a função map(), a filter() recebe dois parâmetros, sendo
# uma função e um iteravel.

res = filter(lambda x: x > media, dados)
print(list(res))

#OBS: Assim como na função map(), após serem utilizados os dados de filter() eles são excluidos da memória.
#print(f'Novamente: {list(res)}')

paises = ['', 'Argentina', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

print(paises)

res = filter(None, paises)

print(list(res))

paises = ['', 'Argentina', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

# res = filter(lambda  pais: len(pais) > 0, paises)
# res = filter(None, paises)
res = filter(lambda  pais: pais != '', paises)

print(list(res))

# A diferença emtre map() e filter() é:

# map() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função para cada eelemento do iterável.

# filter() -> Recebe dois parâmetros, uma função e um iterável e retorna um onjeto filtrando apenas os elementos de acordo com a função.


# Exemplo mais complexo

usuarios = [
    {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': 'carla', 'tweets': ['eu amo gatos']},
    {'username': 'jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': []},
    {'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']},
    {'username': 'gal', 'tweets': []}
]

print(usuarios)

# Filtrar os usuários que estão inativos no Twitter

# Forma 1
# inativos = list(filter(lambda usuario: len(usuario ['tweets']) == 0, usuarios))

# Forma 2
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))

print(inativos)

"""

# Combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)