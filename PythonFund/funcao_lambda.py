# FUNCAO LAMBDA:
'''
- Uma funcao lambda eh uma funcao anonima que nao possui nome.
- Pode ou nao receber argumentos de entrada e retornar um valor de saida.

Sintaxe: 
    
    lambda argumentos: expressao

'''

# Exemplos:

# Exemplo 1: Soma de dois números:
soma = lambda x, y: x + y
print(soma(5, 3))


# Exemplo 2: Quadrado de um número:
quadrado = lambda x: x ** 2
print(quadrado(4))


# Exemplo 3: Filtrar números pares de uma lista:
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)


# Exemplo 4: Dobrar os valores de uma lista:
numeros = [1, 2, 3, 4]
dobrados = list(map(lambda x: x * 2, numeros))
print(dobrados)


# Exemplo 5: Ordenar uma lista de tuplas pelo segundo elemento:
tuplas = [(1, 'b'), (2, 'a'), (3, 'c')]
ordenado = sorted(tuplas, key=lambda x: x[1])
print(ordenado)  


# Exemplo 6: Calcular se um número é maior que outro usando uma funcao lambda:
maior = lambda x, y: x if x > y else y
print(maior(10, 5))


# Exemplo 7: Verificar se uma palavra está em uma lista de palavras:
palavras = ['python', 'lambda', 'função']
existe = lambda palavra: any(palavra in p for p in palavras)
print(existe('lambda'))  
