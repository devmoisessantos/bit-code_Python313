lista_de_jogos = [
    'Star Wars', 'Jedi', 'Naruto', 'Dragon Ball', 'Dragon Ball Z'
]

# 1 - Retornar o tamanho da lista
print(len(lista_de_jogos))

# 2 - Retornar o primeiro elemento da lista
print(lista_de_jogos[0])    

# 3 - Retornar o ultimo elemento da lista
print(lista_de_jogos[-1])

# 4 - Ordenar ou inverter a lista
lista_de_jogos.sort()
print(f'Ordenando a lista: {lista_de_jogos}')

lista_de_jogos.reverse()
print(f'Invertendo a lista: {lista_de_jogos}')

# 5 - Adicionar um elemento na lista
lista_de_jogos.append('Pokemon')
print(f'Adicionando um elemento na lista: {lista_de_jogos}')

# 6 - Remover um elemento da lista
lista_de_jogos.remove('Jedi')
print(f'Removendo um elemento da lista: {lista_de_jogos}')

# 7 - Copiar uma lista
lista_copia = lista_de_jogos.copy()
print(f'Copiando uma lista: {lista_copia}')

# 8 - Concatenar duas listas
lista1 = ['Star Wars', 'Jedi', 'Naruto', 'Dragon Ball', 'Dragon Ball Z']
lista2 = ['Pokemon', 'One Piece', 'Naruto', 'Dragon Ball', 'Dragon Ball Z']
lista3 = lista1 + lista2
print(f'Concatenando duas listas: {lista3}')

# 9 - Recuperar um elemento da lista pelo indice
print(f'Recuperando um elemento da lista pelo indice: {lista_de_jogos}'.index('Dragon Ball'))

# 10 - Remover itens repetidos de uma lista
lista_repetidos = lista3.copy()
lista_sem_repetidos = list(set(lista3))
print(f'Removendo itens repetidos de uma lista: {lista_sem_repetidos}')