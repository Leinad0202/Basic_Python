"""
Funções com Parâmetros Padrão (Default Parameters)

- Funções onde a passagem de parâmetro seja opcional;

# Exemplo de função onde a passagem de parâmetro seja opcional
print('Geek University')

print()

# Exemplo de função onde passagem de parâmetro seja obrigatória

def quadrado(numero):
    return numero ** 2

print(quadrado(3))
print(quadrado()) # TypeError

def exponecial(numero=4, potencia=2):
    return numero ** potencia

print(exponecial(2, 3)) # 2 * 2 * 2
print(exponecial(3, 2)) # 3 * 3 * 3


print(exponecial(3)) # Por padrão eleve ao quadrado
print(exponecial(3, 5)) # Eleva á potência informada pelo usuario

# OBS
# Se o usuário passar somente um argumento, este será atribuido ao parâmetro numero, e será calculado o quadrado número;
# Se o usuário passar 2 argumentos, o primeiro será atribuido ao parâmetro numero e o segundo ao parâmetro potência, então
# será calculada esta potência.

print(exponecial())


# OBS: Em funções Python os parâmetros com valores default (padrão) DEVEM sempre estar ao final da declaração.

# ERRO!
def teste(potencia, num=2):
    return  num ** potencia

print(teste(6))


# Outroas exemplos

def soma(num1=5, num2=3):
    return num1 + num2

print(soma(4, 3))
print(soma(4))
print(soma())


# Exemplo mais complexo

def mostra_informação(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo instrutor Geek'
    elif nome == 'Geek':
        return 'Eu pensei que você fosse o instrutor'
    return f'Olá {nome}'

print(mostra_informação())
print(mostra_informação(instrutor=True))
print(mostra_informação(True))
print(mostra_informação(nome='Ozzy'))

# Por que utilizar parâmetros com valor default?

- Nos permite ser mais flexiveis nas funçãoes;
- Evita erros com parâmetros incorretos;
- Nos permite trabalhar com exemplos mais legiveis de código;

# Quais tipos de dados podemos usar como valores default para parâmetros?

- Qualquer tipo de dado:
    - Nimeros, Strings, Floats, Booleanos, Tuplas, Dicionarios, funções e etc;

 Exemplos

 def soma(num1, num2):
     return  num1 + num2

 def mat(num1, num2, fun=soma):
     return  fun(num1, num2)

 def subtracao(num1, num2):
     return num1 - num2

 print(mat(2, 3))
 print(mat(2, 2, subtracao()))

# Escopo - Evitar problemas e confusões...

# Variáveis globais
# Variáveis locais

instrutor = 'Geek' # Variável global

def diz_oi():
    instrutor = 'Python' # Variável local
    return f'oi {instrutor}'


print(diz_oi())

# OBS: Se tivermos uma variavel local com o mesmo nome de uma variavel global, a locar terá preferência


def diz_oi():
    prof = 'Geek' # Varíavel local
    return f'Olá {prof}'

print(diz_oi())

print(prof) #NameEror


# ATENÇÃO com variaveis globais (Se puder evitar, evite)

total = 0

def incrementa():
    total = total + 1 #UnboundLocalError ( A variável local está sendo usada para processamento sem ter sido inicializada)
    return total

print(incrementa())


# ATENÇÃO com variaveis globais (Se puder evitar, evite)

total = 0

def incrementa():
    global total # Avisando que queremos utilizar a variável global

    total = total + 1
    return total

print(incrementa())
print(incrementa())
print(incrementa())


"""

# Podemos ter funções dentro de funções, e também tem uma forma especial de escopo variável

def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return  contador
    return dentro()

print(fora())
print(fora())
print(fora())

# print(dentro()) #NameError