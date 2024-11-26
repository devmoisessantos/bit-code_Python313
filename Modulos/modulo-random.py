# MODULO RANDOM:

"""
- O modulo random possui diversas funcoes para trabalhar com numeros aleatorios
- Ex: numeros aleatorios, aleatoriedade, etc...

É bastante utilizado para trabalhar com dados, por exemplo:

"""

import random

# 1 - Numeros aleatorios de uma lista:

num = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(
    f'Numero aleatorio entre 1 e 10: {num}'
)

# 2 -Gera um numero aleatorio em um intervalo de valores
num = random.randint(5, 15)
print(
    f'Numero aleatorio entre 5 e 15: {num}'
)

# 3 - Seleciona caracteres aleatorios de uma string:
nome = 'Curso de Python'
letra = random.choice(nome)
print(
    f'Letra aleatoria : {letra}'
)

# 4 - Seleciona mais de um valor aleatorio
# SINTAXE: random.sample(iteravel, valor)
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(
    random.sample(lista, 2)
)
print()
print(
    random.sample(lista, 2)
)

# 5 - Aleatoriedade:
num = random.uniform(1, 10)
print(
    f'Numero aleatorio entre 1 e 10: {num}'
)

# 4 - Aleatoriedade:
num = random.randrange(1, 10)
print(
    f'Numero aleatorio entre 1 e 10: {num}'
)

