# EXERCICIO 9:
# - Contar Minusculas:
# - Contar Maiusculas:

'''
Escreva uma funcao em Python que receba uma String e conte o 
numero de letras maiusculas e minusculas desta string.

'''
def contar_letras(string):
    minusculas = 0
    maiusculas = 0
    contagem_letras = {}                       # Dicionário para contar as ocorrências das letras

    for \
        letra in string:
        if \
            letra.islower():                   # Verifica se a letra é minúscula
            minusculas += 1
            if \
                letra in contagem_letras:      # Se a letra já foi vista, incrementa a contagem
                contagem_letras[letra] += 1
            else:                              # Se a letra ainda não foi vista, inicializa a contagem
                contagem_letras[letra] = 1
        elif \
            letra.isupper():                   # Verifica se a letra é maiúscula
            maiusculas += 1
            if \
                letra in contagem_letras:      # Se a letra já foi vista, incrementa a contagem
                contagem_letras[letra] += 1
            else:                              # Se a letra ainda não foi vista, inicializa a contagem
                contagem_letras[letra] = 1
        else:
            pass                               # Se não for uma letra, não faz nada

    # Exibe a contagem das letras
    for \
        letra, contagem in contagem_letras.items():
        print(f'{letra}: {contagem}')

    print(f'Quantidade de letras minúsculas: {minusculas}')
    print(f'Quantidade de letras maiúsculas: {maiusculas}')

# Testando a função
contar_letras('Python')
