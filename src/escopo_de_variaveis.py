"""
Escopo de variaveis

Dois casos de escopo:

1 - Variáveis globais;
    - variaveis globais são reconhecidas, ou seja, seu escopo compreende, todo o programa.

2 - Variáveis locais;
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
    esta limitado ao bloco onde foi declarada.

para declarar variáveis em python fazemos:

nome_da_variavel = valor_da_variavel

Python é uma linguegem de tipagem dinâmica. Isso significa que
 ao declararmos uma variável, nós não colocamos o tipo de dado dela.
 Este tipo é inferido ao atribuirmos o valor à mesma.

 Exemplo em C:
 int numero = 42;

 exemplo em Java:
 int numero = 42;

"""

numero = 'Geek'   #Exemplo de variável global
print(numero)
print(type(numero))

numero = 42       #Exemplo de variável global
print(numero)
print(type(numero))


if numero > 10:
    novo = numero + 10 # A variável 'novo' está declarada localmente dentro do bloco do if. Portanto, é local
    print(novo)