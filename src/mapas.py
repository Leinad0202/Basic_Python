"""
Mapas -> Conhecidos em python como Dicionários

Dicionários em python são representados por chaves {}


# Interar sobre dicionários
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')

# Acessando as chaves

print(receita.keys())

for chave in receita.keys():
    print(receita[chave])


# Acessando os valores

print(receita.values())

for valor in receita.values():
    print(valor)


# Desempacotamento de dicionários

for chave, valor in receita.items():
    print(f'chave = {chave} e valor = {valor}')


receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita)

# Soma*, Valor Maximo*, Valor Minimo*, Tamanho

# * Se os valores forem todos inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))

"""

# Importante lembrar que, além de não termos valores duplicados, não temos ordem

