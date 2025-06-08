"""
Definindo Funções

- Funções são pequenas partes de códigos que realizam tarefas específicas;
- Pode ou não receber entrada de dados e retornar uma saída de dados;
- Muitos uteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela;
é bom fazer uma verificação para que a função seja simplificada

Já utilizamos várias funções desde que iniciamos este curso:
- print()
- len()
- max()
- min()
- count()
- e muitas outras;


"""

# Exemplo de utilização de funções

#cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (Build-in) do Python

#print(cores)

#curso = 'Programação Em Python: Essencial'

#print(curso)

#cores.append('roxo')

#print(cores)

# curso.append('mais dados...') # AttributeError
# print(curso)

#cores.clear()
#print(cores)


# print(help(print()))

# DRY - Don't Repeat Youtself - Não repita você mesmo / não repita seu código.

# Mas então, como definir funções?

"""
Em Python, a forma geral de definir uma função é:

def nome_da_funcao(parametro_de_entrada):
    bloco_da_funcao
    
    
onde:

nome_da_funcao -> SEMPRE, com letras minúsculas, e se for nome composto, separado por underline(Snake Case);
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não;
bloco de função -> Também chamado de corpo da função ou implementação, é onde o precessamento da função acontece.
Neste bloco, pode ter ou não retorno da função

OBS: Veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao Python que
estamos definindo uma função, também abrimos o bloco de código com o já conhecido dois pontos : que é
utilizado em python para definir blocos.


"""

# Definindo a primeira função

# def diz_oi():
  #  print('oi!')


"""
OBS:

1 - Veja que, dentro das nossas funções podemos utilizar outras funções;
2 - Veja que nossa função executa 1 tarefa, ou seja; a unica coisa que ela faz é dizer oi;
3 - Veja que esta função não recebe nenhum parametro de entrada;
4 - Veja que está funçao não retorna nada;
"""

# Utilizando funções

# Chamada de execução
# diz_oi()

"""
ATENÇÃO:

Nunca esqueça de utilizar o parênteses ao executar uma função.

Exempllo

# Errado
diz_oi

# Certo
diz_oi()

# Errado
diz_oi ()
"""

# Exemplo 2

def cantar_parabens():
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('muitos anos de vida')
    print('viva o aniversariante!')


# for n in range(5):
  #  cantar_parabens()

# Em Python, podemos inclusive criar variaveis do tipo de uma função e executar esta função através da varíavel

canta = cantar_parabens()
print(canta)
