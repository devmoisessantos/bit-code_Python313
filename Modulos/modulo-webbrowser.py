import os
import webbrowser
from time import sleep

"""
    Modulo webbrowser:
    - Abre o navegador padrao do sistema operacional

    
Programa abrindo sites na Web:
"""

def limpar_tela():
    os.system('cls')

pronto = False

while not pronto:
    print(
        'O que deseja fazer?\n\n'

        '1 - Abrir o Google\n'
        '2 - Abrir o YouTube\n'
        '3 - Abrir a Documentação Python\n'
        '4 - Abrir o GitHub\n'
        '7 - Sair\n'
    )
    print('Escolha uma opção:')
    escolha = input('>>> ')

    if escolha == '1':
        limpar_tela()
        webbrowser.open('https://www.google.com.br')

    elif escolha == '2':
        limpar_tela()
        webbrowser.open('https://www.youtube.com')

    elif escolha == '3':
        limpar_tela()
        webbrowser.open('https://docs.python.org/pt-br/3/')

    elif escolha == '4':
        limpar_tela()
        webbrowser.open('https://github.com')

    elif escolha == '7':
        limpar_tela()
        pronto = True

    else:
        limpar_tela()
        print(
            'Opção inválida...'
            'Tente uma opção válida.')
        sleep(2)
        limpar_tela()
