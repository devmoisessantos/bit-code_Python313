# EXERCICIO 4:
# - Adivinhe qual o numero:

'''
Escreva um programa em Python que gere um numero aleatorio
para que o usuario tente acertar o numero gerado.

1 - Utilizar um laço de repeticao para que o programa execute até 
que o usuario informe um numero referente a opçao para sair do programa.

2- Utilizar o modulo RANDOM  para gerar valores aleatorios dentro de
um intervalo de valores.
Ex:
    1 a 10.

3 - Lê o numero que o usuario digitar via input e comparar se 
é o numero que o programa gerou.

'''

import os
import random
from time import sleep


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def sair():
    print("Encerrando...")
    sleep(2)
    exit()


acertou = False
escolheu = ''
escolha = False
escolha_invalida = False

while not acertou:
    print(
        'Adivinhe qual o número: \n\n'
        '1 - Jogar \n'
        '2 - Sair \n'
        '\n'
        'Selecione uma opção: '
    )
    escolheu = input('>>> ')
    escolha = escolheu.isnumeric() 
    escolha_invalida = not escolha

    if escolha_invalida:
        limpar_tela()
        print('Digite uma opção válida...')
        sleep(1.5)
        limpar_tela()
        continue  # Volta ao início do menu

    # Conversão da entrada para número
    escolheu = int(escolheu)

    if escolheu == 2:
        limpar_tela()
        sair()

    elif escolheu == 1:
        limpar_tela()
        numero_aleatorio = random.randint(1, 10)
        while not acertou:
            try:
                chute = int(input('Adivinhe o número entre 1 e 10: '))
                if chute == numero_aleatorio:
                    acertou = True
                    limpar_tela()
                    print('Parabéns! Você acertou.')
                    break
                elif chute < numero_aleatorio:
                    print('Tente um número maior.')
                else:
                    print('Tente um número menor.')
            except ValueError:
                print('Por favor, insira um número válido.')
    else:
        limpar_tela()
        print('Digite uma opção válida...')
        sleep(1.5)
        limpar_tela()
