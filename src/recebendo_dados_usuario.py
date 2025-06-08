"""
Recebendo dados do usuário

input -> todd dado recebido via input é do tipo string
"""
# Entrada de dados
print('qual seu nome?')
nome = input()  # input -> Entrada

# print('Seja bem-vindo(a) %s' % nome)
# print('Seja bem-vindo(a) {0}' .format(nome))

#Exemplo de print mais atual V3.7
print(f'Seja bem-vindo(a) {nome}')

print('Qual sua idade?')
idade = int(input())
# processamento

# Saída de dados
# print('A %s tem %s anos' % (nome, idade))
# print('A {0} tem {1} anos' .format(nome, idade))

#Exemplo de print mais atual V3.7
print(f'{nome} tem {idade} anos')

print(f'{nome} nasceu em {2024 - int(idade)}')