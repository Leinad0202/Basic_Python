"""
Estruturas Lógicas: and (e), or (ou), not (não), is (é)

Operadores unários:
    - no;
Operadores binários:
    - and, or, is

Regras de funcionamentos:

Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor do booleano é invertido, ou seja, se for True, vira False, se for False vira True
Para 'is', o valor é comparado com um segundo.

"""

ativo = False
logado = False

# Se não estiver ativo
if not ativo:
    print('Você precisa ativar sua conta. por favor, cheque seu e-mail')
else:
    print('Bem-vindo usuário')

#ativo é verdadeiro?
print(ativo is True)