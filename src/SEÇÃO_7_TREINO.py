"""
 1. Crie um programa que tenha uma função que recebe um parâmetro inteiro e devolve o seu dobro.

def dobro(num1):
    return num1 * 2

entrada = int(input('Digite um numero: '))

print(dobro(entrada))

 2. Faça um programa que tenha uma função que recebe uma data no formato string exemplo “01/01/2024” e
imprima ela por extenso como “1 de janeiro de 20204”.

def data(dia, mes, ano):
    meses = {
        'janeiro': 'janeiro',
        'fevereiro': 'fevereiro',
        'março': 'março',
        'abril': 'abril',
        'maio': 'maio',
        'junho': 'junho',
        'julho': 'julho',
        'agosto': 'agosto',
        'setembro': 'setembro',
        'outubro': 'outubro',
        'novembro': 'novembro',
        'dezembro': 'dezembro'
    }
    mes_formatado = mes.lower()
    if not dia.isdigit():
        raise ValueError('Dia invalido, digite o dia corretamente!')
        return

    if not ano.isdigit():
        raise ValueError('Ano invalido, digite o ano corretamente!')
        return

    if mes_formatado not in meses:
        raise ValueError('Mês invalido, digite o mês corretamente!')
        return

    print(f'{dia} de {mes} de {ano}')

try:
    dia = input('fale o dia:')
    mes = input('fale o mes')
    ano = input('fale o ano')

    resultado = data(dia, mes, ano)
    print(resultado)

except ValueError as erro:
    print(erro)

 3. Faça um programa que tenha uma função que receba uma lista de inteiros e retorne o maior valor


def maior_valor(lista):
    maior = lista[0]

    for numero in lista:
        if numero > maior:
            maior = numero
    return maior

lista = [1, 2, 3, 4, 9, 6, 7]

print(maior_valor(lista))

"""

def data_por_extenso(data:str) -> None:
    d = data.split('/')

    dia: int = int(d[0])
    mes: int = int(d[1])
    ano: int = int(d[2])

    meses = {
        1: 'janeiro',
        2: 'fevereiro',
        3: 'março',
        4: 'abril',
        5: 'maio',
        6: 'junho',
        7: 'julho',
        8: 'agosto',
        9: 'setembro',
        10: 'outubro',
        11: 'novembro',
        12: 'dezembro'
    }

    print(f'{dia} de {meses[mes]} de {ano}')

if __name__ == '__main__':
    data_por_extenso('01/01/2024')