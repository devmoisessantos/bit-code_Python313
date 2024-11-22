# CONHECENDO AS LISTAS EM PYTHON:
'''
- Uma lista em Python é uma estrutura de dados que permite armazenar e manipular uma coleção de elementos.
     Listas sao mutáveis, ou seja, podem ser modificadas depois de criadas.
- As listas em Python podem ser criadas usando colchetes [].
Alem disso, também podem ser criadas usando a funcao list().
'''

# Trabalhando com listas:

# Criando uma lista vazia:

lista_vazia = []

# Criando uma lista com elementos:
'''
Listas podem ser criadas com elementos dos tipos:

- inteiros = int() '0'
- floats = float() '0.0'
- strings = str() '" "'
- booleanos = True or False
- listas = list() '[]'
- tuplas = tuple() '()'
- dicionarios = dict() '{}'
- conjuntos = set() '{}'

'''

lista_com_elementos = [1, 2.0, 'Python', True, [1, 2, 3],
                        (1, 2, 3),
                        {'a': 1, 'b': 2},
                          {1, 2, 3},
                            {1: 'a', 2: 'b', 3: 'c'}]

for i, j in enumerate(lista_com_elementos):
    print(f'{i}: {j} -----------------------> TIPO:', type(j))
print()

# Removendo um elemento da lista:
del lista_com_elementos[8]

for i, j in enumerate(lista_com_elementos):
    print(f'{i}: {j} -----------------------> TIPO:', type(j))

print()

# Filtrando elementos de uma lista:
lista_filtrada = [i for i in lista_com_elementos if type(i) == str]
print(f'Lista filtrada de strings: {lista_filtrada}')

lista_filtrada = [i for i in lista_com_elementos if type(i) == float]
print(f'Lista filtrada de float: {lista_filtrada}')

lista_filtrada = [i for i in lista_com_elementos if type(i) == dict]
print(f'Lista filtrada de dicionarios: {lista_filtrada}')

lista_filtrada = [i for i in lista_com_elementos if type(i) == int]
print(f'Lista filtrada de inteiros: {lista_filtrada}')

lista_filtrada = [i for i in lista_com_elementos if type(i) == set]
print(f'Lista filtrada de conjuntos: {lista_filtrada}')

lista_filtrada = [i for i in lista_com_elementos if type(i) == bool]
print(f'Lista filtrada de booleanos: {lista_filtrada}')

lista_filtrada = [i for i in lista_com_elementos if type(i) == tuple]
print(f'Lista filtrada de tuplas: {lista_filtrada}')

lista_filtrada = [i for i in lista_com_elementos if type(i) == list]
print(f'Lista filtrada de listas: {lista_filtrada}')

# SLICING COM LISTAS:

# De maneira similar a Strings,
# podemos utilizar o slicing para extrair partes de uma lista.

'''
Ex:

lista_de_jogos = ['Star Wars', 'Jedi', 'Naruto', 'Dragon Ball', 'Dragon Ball Z']

print(lista_de_jogos[0:3])  # ['Star Wars', 'Jedi', 'Naruto']
print(lista_de_jogos[2:])  # ['Naruto', 'Dragon Ball', 'Dragon Ball Z']
print(lista_de_jogos[:3])  # ['Star Wars', 'Jedi', 'Naruto']
print(lista_de_jogos[:])  # ['Star Wars', 'Jedi', 'Naruto', 'Dragon Ball', 'Dragon Ball Z']

'''
print()

# Concatenando listas:

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [7, 8, 9]

print(f'Concatenando listas: {lista1 + lista2 + lista3}')

# Repetindo listas:

print(f'Repetindo listas: {lista1 * 3}')

# Verificando se um elemento pertence a uma lista:

print(f'Verificando se um elemento pertence a uma lista: {4 in lista1}')

print(f'Verificando se um elemento pertence a uma lista: {4 not in lista1}')

# Verificando se uma lista pertence a outra:

print(f'Verificando se uma lista pertence a outra: {lista1 in lista_com_elementos}')

print(f'Verificando se uma lista pertence a outra: {lista1 not in lista_com_elementos}')

# Verificando o tamanho de uma lista:

print(f'Verificando o tamanho de uma lista: {len(lista_com_elementos)}')

# Invertendo uma lista:

print(f'Invertendo uma lista: {lista_com_elementos[::-1]}')

# Copiando uma lista:

print(f'Copiando uma lista: {lista_com_elementos.copy()}')

# Removendo elementos de uma lista:

print(f'Removendo elementos de uma lista: {lista_com_elementos.remove(2)}')

print(f'Removendo elementos de uma lista: {lista_com_elementos}')