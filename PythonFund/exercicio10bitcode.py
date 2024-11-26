# EXERCICIO 10:
# - Lista numeros pares e impares em uma lista: 

'''
Escreva uma funcao em Python que imprima uma lista de numeros pares e uma lista de numeros impares.
- As listas devem ser separadas, ou seja lista_pares[] e lista_impares[].

'''

def lista_pares_impares(lista_numeros):
    # Funções lambda para verificar se o número é par ou ímpar
    is_pares = lambda x: x % 2 == 0
    is_impares = lambda x: x % 2 != 0

    # Usando filter com lambda para separar os pares e ímpares
    lista_pares = list(filter(is_pares, lista_numeros))
    lista_impares = list(filter(is_impares, lista_numeros))

    return lista_pares, lista_impares

# Exemplo de uso da função
lista = list(range(1, 11))  # Lista de números de 1 a 100
pares, impares = lista_pares_impares(lista)

# Imprimir as listas
print('Pares:', pares)
print('Impares:', impares)
