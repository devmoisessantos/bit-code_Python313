# REPETICOES EM PYTHON COM LAÇO WHILE:
'''
- Uma repetição em Python com laço while consiste em executar um bloco de instruções
'enquanto' uma condição for verdadeira.

- Se a condição nunca se tornar falsa, o laço será executado indefinidamente.

- O laço while consiste em uma estrutura de controle que itera sobre uma
condição que deve ser satisfeita para que o bloco de instruções seja executado.

'''

# Sintaxe Básica
condicao = '''

- condição: Uma expressão que deve ser avaliada como verdadeira (`True`) para que o bloco seja executado.
- O laço continua executando até que a condição se torne falsa (`False`).

'''

while True:
    # Bloco de código a ser executado enquanto a condição for verdadeira
    break


contador = 0
while contador < 5:
    print(f'Contador: {contador}')
    contador += 1

# Controlando o Fluxo no Laço WHILE

# break

numero = 0
while numero < 10:
    if numero == 5:
        break
    print(numero)
    numero += 1

# continue

numero = 0
while numero < 5:
    numero += 1
    if numero == 3:
        continue
    print(numero)

# Cuidado com Loops Infinitos

# while True:
#     print("Isso é um loop infinito!")

'''_________________________________________________________'''

import random

numero_secreto = random.randint(1, 10)
tentativas = 0

while True:
    chute = int(input("Adivinhe o número entre 1 e 10: "))
    tentativas += 1
    if chute == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break
    elif chute < numero_secreto:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")