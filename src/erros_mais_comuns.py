"""
Erros mais comuns em Python

È importante prestar atenção e aprender a ler as saídas de erros geradas pela execução
do nosso código.

Os erros mais comuns:

1 - SyntaxErro -> Ocorre quando o Python encontra um erro de sintaxe. Ou seja, você escreveu algo que o Python não reconhece como parte da linguagem.

Exemplo SyntacError

A)

def funcao:
    print('olá')

B)

def = 1

C)

return

2 - NameError -> Ocorre quando uma variável ou uma função não foi definida

Exemplos NameError

a)
print(geek)

B)
geek()

C)
a = 18

if a < 10:
    msg = 'é maior que 10'

print(msg)

3 - TypeError -> Ocorre quando uma função/ operação/ ação é aplicado a um tipo errado.

Exemplos TypeError

A)
print(len(5))

B)
print('Geek' + [])

4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lisra ou outro tipo de dado indexado utilizando
um índice válido

Exemplos IndexError

a)
lista = ['Geek']
print(lista[2])

b)
lista = ['Geek']
print(lista[0][10])

c)
lista = ('Geek')
print(lista[0][10])


5 - ValueError -> ocorre quando uma função/operação built-in (integrada) recebe um argumento com tipo correto
mas valor inapropriado.

Exemplos ValueError

A)
print(int('Geek'))


6 - KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe.

Exemplos KeyError

A)
dic = {'python': 'university'}
print(dict['geek'])


7 - AttributeError -> Ocorre quando uma variável não tem um atributo/função

Exemplos AttributeError

A)

tupla = (11, 2, 31, 4)
print(tupla.sort())


8 - IndentationError -> Ocorreu quando não respeitamos a indentação do Python (4 espaços)

Exemplos IndentationError

A)
def nova():
print('Geek')

nova()

B)
for i in range(10):
i+1

print(i)


OBS: Exceptions e Errors são sinônimos na programação

OBS: Importante ler e prestar atenção na saída de Error
"""

