"""
Módulo Collections - Counter (Contador)

Collections -> High-performance Container Datetype


Counter -> Recebe um interavel como papâmetro e cria um objeto do tipo collections Counter que é parecido
com um dicionário, cpmtamdp cp,p chave o elemento da lista passada como parâmetro e como valor a quantidade de ocorrências desse elemento.

# Utilizando Counter

# Exemplo 1

# Podemos utilizar qualquer iterável, aqui usamos uma Lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

# Utilizamos o Counter
res = Counter(lista)

print(type(res))

print(res)

# Counter({1: 5, 3: 5, 2: 4, 5: 4, 4: 3, 45: 2, 66: 2, 43: 1, 34: 1})

# Veja que, para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrências.

# Exemplo 2

print(Counter('Geek University'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

"""

from collections import  Counter

# Exemplo 3

texto = """Python é uma linguagem de programação de alto nível,[10] interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991.
[1] Atualmente, possui um modelo de desenvolvimento comunitário, aberto e gerenciado pela organização sem fins lucrativos Python Software Foundation.
 Apesar de várias partes da linguagem possuírem padrões e especificações formais, a linguagem, como um todo, não é formalmente especificada. O padrão na pratica é a implementação CPython.
A linguagem foi projetada com a filosofia de enfatizar a importância do esforço do programador sobre o esforço computacional. Prioriza a legibilidade do código sobre a velocidade ou expressividade.
 Combina uma sintaxe concisa e clara com os recursos poderosos de sua biblioteca padrão e por módulos e frameworks desenvolvidos por terceiros.
Python é uma linguagem de propósito geral de alto nível, multiparadigma, suporta o paradigma orientado a objetos, imperativo, funcional e procedural.
 Possui tipagem dinâmica e uma de suas principais características é permitir a fácil leitura do código e exigir poucas linhas de código se comparado ao mesmo programa em outras linguagens. Devido às suas características,
  ela é utilizada, principalmente, para processamento de textos, dados científicos e criação de CGIs para páginas dinâmicas para a web. Foi considerada pelo público a 3ª linguagem "mais amada",
   de acordo com uma pesquisa conduzida pelo site Stack Overflow em 2018[11] e está entre as 5 linguagens mais populares, de acordo com uma pesquisa conduzida pela RedMonk.[12]
O nome Python teve a sua origem no grupo humorístico britânico Monty Python,[13] criador do programa Monty Python's Flying Circus,
 embora muitas pessoas façam associação com o réptil do mesmo nome (em português, píton ou pitão)."""

palavras = texto.split()

# Print(Palavras)

res = Counter(palavras)

print(res)

# Encontrando as 5 palavras com mais ocorrencia no texto
print(res.most_common(5))