"""
**kwargs

Poderíamos chamar este parâmetro de **xix, mas por convenção chamamos de **kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca valores extra
em uma tupla, o **kwargs exige que utilizemos parÂmetros nomeados, e transforma esses parâmetros extras em um dicionário


# Exemplo

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')

cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# OBS: Os parâmetros *args e **kwargs não são obrigatórios.

cores_favoritas()

cores_favoritas(geek='navy')


# Exemplo mais complexo

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs ['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythonico Geek'
    elif 'geek' in kwargs:
        return f"{kwargs ['geek']} Geek"
    return 'não tenho certeza quem você é...'


print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='oi'))
print(cumprimento_especial(geek='especial'))


# Nas nossas funções, podemos ter(NESTA ORDEM):

- Parâmetros obrigatorios;
- *args;
- Parâmetros default (não obrigatórios);
- **kwargs;


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(8, 'julia')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(38, 'Felipe', eu='não', vice='vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True )


# Entenda por quê é importante manter a ordem dos parâmetros na declaração


# Função com a ordem correta de parâmetros
#def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
#    return [a, b, args, instrutor, kwargs]

# Função com a ordem incorreta de parâmetros
#def mostra_info(a, b, instrutor='Geek', *args, **kwargs):
#    return [a, b, args, instrutor, kwargs]

#print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))


a= 1
b= 2
args = (3,)
kwargs = {'sobrenom': 'University', 'cargo': 'Instrutor'


# Desempacotar com **kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}

print(mostra_nomes(**nomes))

"""

def soma_multiplos_numeros(a, b, c, **kwargs):
    print(a + b + c)

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3)

soma_multiplos_numeros(**dicionario)

#OBS! Oa nomes das chaves em um dicionario devem ser o mesmo dos parâmetros da função

#dicionario = dict(d=1, e=2, f=3)
#soma_multiplos_numeros(**dicionario)

dicionario = dict(a=1, b=2, c=3, nome='Geek')

soma_multiplos_numeros(**dicionario, lang='Python')