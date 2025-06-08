"""
Módulo Collections - Default Dict

# Repcap Dicionários


dicionario = {'curso': 'Programação em Python: Essencial'}

print(dicionario)

print(dicionario['curso'])

Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default,
podendo utilizar um lambda para isso, Este valor será utilizado sempre que não houver
um valor definido, Caso tentemos acessar um chave que não existe, essa chave será
criada e p valor default será atribuido

OBS: Lambdas são funções sem nome, que podem ou não receber parametros de entrada
e retornar valores.

"""

# Fazendo import
from collections import  defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programação em Python: Essencial'

print(dicionario)

print(dicionario['outro']) # KeyError no dicionário comum, mas aqui não.

print(dicionario)