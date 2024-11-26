# FUNCOES COM ARGUMENTOS KEYWORD:
"""
*kwargs - Argumentos nomeados variaveis
- Alem dos valores podemos passar tambem as respectivas 
chaves paraa cada argumento.

- Os argumentos sao passados como um dicionario.

"""

def funcao(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

funcao(a=1, b='2a', c='3c')
funcao(d=4, e=5, f=6)

