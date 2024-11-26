# REPETICOES EM PYTHON COM LAÇO FOR:
'''
- Uma repetição em Python com laço for consiste em executar um bloco de instruções
um certo número de vezes.

- O laço for em Python consiste em uma estrutura de controle que itera sobre uma
coleção de elementos, executando um bloco de instruções para cada elemento da coleção.

'''

# Iterando sobre uma string:

for letra in 'Python':
    print(letra) # P y t h o n

# Iterando sobre uma lista:

for numero in [1, 2, 3, 4, 5]:
    print(numero) # 1 2 3 4 5

# Quando a iteração for é satisteita o loop para.

# BREAK:

for numero in [1, 2, 3, 4, 5]:
    if numero == 3:
        break
    print(numero) # 1 2

# CONTINUE:

for numero in [1, 2, 3, 4, 5]:
    if numero == 3:
        continue
    print(numero) # 1 2