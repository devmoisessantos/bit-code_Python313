# LIST COMPREHENSION:
'''
- Uma list comprehension em Python consiste em uma estrutura de controle que itera sobre uma
coleção de elementos, executando um bloco de instruções para cada elemento da coleção.

- O resultado da list comprehension é uma nova lista que contém os resultados das expressões
que foram avaliadas.

'''

# Sintaxe Básica:

'''
variavel = [ expressão  for  item  in  sequência ]
variavel = [ expressão  for  item  in  sequência  if  condicional ]

'''

# Exemplo:

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = [numero for numero in numeros if numero % 2 == 0]

print(pares)

impares = [numero for numero in numeros if numero % 2 != 0]

print(impares)

# LIST COMPREHENSION COM ELSE:
print('\n')


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = [
    f'Par: {i+1}' if numero % 2 == 0 
    else f'Impar: {i+1}' for i, numero in enumerate(numeros)
]

while pares: 
    print(pares.pop(0))

# LIST COMPREHENSION COM DICT:
print('\n')

numeros = [int(i) for i in list(range(1, 11))]
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]     mais dificil kkkkkk

pares = {
    numero: 'Par' if numero % 2 == 0 
    else 'Impar' for numero in numeros
}

for chave, valor in pares.items(): 
    print(f'Chave: {chave}, Valor: {valor}') 