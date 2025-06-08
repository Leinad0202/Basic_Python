"""
Documentando funções com Docstings

OBS: Podemos ter acesso á documentação de uma função em python
utilizando a propriedade especial __doc__
"""

# Exemplos

def diz_oi():
    """Uma função simples que retorna a string 'oi!'"""
    return 'Oi!'

def exponencial(numero, potencia=2):
    """
    função que retorna por padrão o quadrafo 'numero' ou 'numero á 'potencia' informada.
    :param numero: Número que desejamos gerar o exponencial.
    :param potencia: Potência que queremos gerar o exponencial. por padrão é 2
    :return: Retorna o exponencial de 'numero' po 'potencia'.
    """
    return numero ** potencia