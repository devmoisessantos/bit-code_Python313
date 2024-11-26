# FUNCOES COM ARGUMENTOS:
"""
*args - Argumentos posicionais variaveis
 Utilizamos ele quando nao temos certeza de quantos argumentos serao passados 
 para a funcao.
 - Os argumentos serao armazenados em uma tupla
  
"""

def soma(*num):
    soma_total = 0
    for n in num:
        soma_total += n
    print(f'Somando os valores {num} temos {soma_total}!') 

soma(2, 5, 5, 5, 3)

