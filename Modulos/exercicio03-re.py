# EXERCICIO 3:
"""
Desenvolver um Programa que receba um texto/frase/palavra e verifique se essa String 
possui apenas um determinado conjunto de caracteres.

Exemplo:
(a - z); (A - Z); (0 - 9)
"""

import re

# Padrões para letras minúsculas, maiúsculas e números
padrao_min = r'^[a-z]+$'
padrao_mai = r'^[A-Z]+$'
padrao_num = r'^[0-9]+$'

# Entrada do usuário
string = input('Digite uma palavra/frase/texto: ').strip()

# Verificar se a entrada está vazia
if not string:
    print('Você precisa digitar uma palavra/frase/texto.')

else:
    # Determinar se é palavra, frase ou texto
    palavras = string.split()
    num_palavras = len(palavras)
    comprimento = len(string)

    if num_palavras == 1:
        print(f'A entrada "{string}" é uma palavra.')
        if re.fullmatch(padrao_min, string):
            print(f'A palavra "{string}" contém apenas letras minúsculas.')

        elif re.fullmatch(padrao_mai, string):
            print(f'A palavra "{string}" contém apenas letras maiúsculas.')

        elif re.fullmatch(padrao_num, string):
            print(f'A palavra "{string}" contém apenas números.')

        else:
            print(f'A palavra "{string}" contém caracteres mistos.')

    elif num_palavras > 1 and num_palavras <= 30:
        print(f'A entrada é uma frase com {num_palavras} palavras.')

    elif num_palavras > 30:
        print(f'A entrada é um texto com {num_palavras} palavras.')

    # Verificar se contém apenas letras ou números
    if re.fullmatch(r'^[a-zA-Z0-9 ]+$', string):
        print(f'A entrada "{string}" contém apenas letras e/ou números.')

    else:
        print(f'A entrada "{string}" contém caracteres especiais.')
