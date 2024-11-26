from collections import Counter, namedtuple, deque
from operator import itemgetter

# 1 - Contar itens de uma lista

frutas = [
    'banana', 'abacaxi', 'tangerina', 'banana', 
    'banana', 'abacaxi', 'banana', 'maçã',
    'uva', 'uva', 'uva', 'uva', 'uva',
    'laranja', 'laranja', 'laranja', 'laranja',
    'tangerina', 'tangerina', 'tangerina', 'tangerina',
    'pera', 'pera', 'pera', 'pera'
]

print(Counter(frutas))
print()
print(frutas)
print()

# 2 - Utilizando tupla nomeada 

game = namedtuple('game', ['nome', 'preco', 'genero'])
jogo_um = game('GTA VC', 60, 'Aventura')
jogo_dois = game('GTA 3', 100, 'Aventura')
jogo_tres = game('GTA SA', 35, 'Aventura')
jogo_quatro = game('GTA V', 70, 'Aventura')

print(jogo_um)
print()
print(jogo_dois)
print()
print(jogo_tres)
print()
print(jogo_quatro)
print()

# 3 - Ordenando dicionarios

estudantes = {
    
    'Moises': 26,
    'João': 18,
    'Maria': 19,
    'Joaquim': 20,
    'Joana': 21
}

ordenado = sorted(estudantes.items(), key=itemgetter(0))
print()
print(estudantes)
print()
print(ordenado)
print()

# 4 - Utilizamdo fila ambas extremidades

fila = deque([20, 40, 10, 30, 50, 70, 90, 60, 80, 100])
fila.appendleft([1,])
print()
print(fila)
print()
fila.append(200)
fila.popleft()
print()
print(fila)
fila.pop()
print()
print(fila)
print()