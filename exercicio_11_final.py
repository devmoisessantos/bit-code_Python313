# EXERCICIO 11:
"""
PROJETO:
- Gerenciamento de jogadores e times:

Escreva um programa em Python que realize o gerenciamento de  Jogadores.
- Ele deve atender aos seguintes requisitos:

1. A opcao de listar os times deve mostrar o indice, o nome e 
a quantidade de jogadores de cada time.
2. A opcao de adicionar um time deve pedir um nome 
para o time que sera adicionado.
3. A opcao de remover um time deve pedir o indice especifico 
do time que foi cadastrado para ser removido.
4. A opcao de adicionar um jogador deve pedir o indice do time que 
foi cadastrado e assciar com o nome do jogador que sera adicionado.
5. A opcao de remover um jogador em um time deve pedir o indice do time 
que foi cadastrado e o indice do jogador que sera removido.
6. A opcao de listar os jogadores de um time deve pedir o indice 
do time que foi cadastrado e mostrar o indice,
o nome de cada jogador e a quantidade total de jogadores nesse time[indice].

"""

from time import sleep
import os
entrada = ''
def menu():
    print(

        'Gestão de times de futebol:\n\n'\
        '1 - Listar times\n'\
        '2 - Adicionar time\n'\
        '3 - Remover time\n'\
        '4 - Adicionar jogador\n'\
        '5 - Remover jogador\n'\
        '6 - Listar jogadores de um time\n'\
        '7 - Sair\n'
    )
    print('Escolha a interação desejada:')

def limpar_tela():
    os.system('cls')


times = {}
escolha = None
nome_time = None
novo_time = None


def listar_times():
    if len(times) == 0:
        print(

            'Gestão de times de futebol:\n\n'\
            'Nenhum time pra ser listado!\n\n'
        )
        print(
            'Voltando ao menu principal...'
        )
        sleep(2.5)
        limpar_tela()
        return

    print(
            'Gestão de times de futebol:\n\n'\
            'Listar times:\n\n'\
    )
    for i, (nome, jogadores) in enumerate(times.items()):
        
        print(
            f'T-00{i} - Clube: {nome} - Jogadores: {len(jogadores)}'
        )

    print(
        '\nPressione Enter para voltar:'
    )

    while True:
        escolha = input('>>> ').strip()
        if escolha == '':
            limpar_tela()
            return

        else:
            print('Opção inválida...')
            sleep(2)
            limpar_tela()


def adicionar_time():
    print(
        'Gestão de times de futebol:\n\n'\
        'Adicionar time:\n\n'

        '1 - Cancelar\n\n'
        'Digite 1/Enter para cancelar\n\n'\
        'Digite o nome do time que deseja adicionar:'
    )
    novo_time = input('>>> ')

    if novo_time == '1' or novo_time == '':
        limpar_tela()
        print(

            'Gestão de times de futebol:\n\n'\
            'Nenhum time adicionado!\n\n'
        )
        print(
            'Voltando ao menu principal...'
        )
        sleep(1.5)
        limpar_tela()
        return

    elif novo_time in times:
        limpar_tela()
        print(
            'Gestão de times de futebol:\n\n'\
            f'O time: {novo_time} ja foi cadastrado!\n\n'
        )
        print(
            'Voltando ao menu principal...'
        )
        sleep(1.5)
        limpar_tela()
        return

    elif novo_time not in times:
        if novo_time.isalpha():
            limpar_tela()
            times[novo_time] = []  
            print(
                'Gestão de times de futebol:\n\n'\
                f'O time: {novo_time} foi adicionado a lista.!\n\n'
            )
            print(
                'Voltando ao menu principal...'
            )
            sleep(1.5)
            limpar_tela()
            return
        else:
            limpar_tela()
            print(
                'Gestão de times de futebol:\n\n'\
                'Nome do time inválido!\n\n\n'
                'Retornando ao menu principal...'
            )
            sleep(1.5)
            limpar_tela()
    else:
        print('Opção inválida...')
        sleep(2)
        limpar_tela()

def remover_time():
    if not times:
        print(
            'Gestão de times de futebol:\n\n'\
            'Nenhum time cadastrado!\n\n'
            'Voltando ao menu principal...'
        )
        sleep(2.5)
        limpar_tela()
        return
    
    print(
        'Gestão de times de futebol:\n\n'\
        'Remover time:\n'
        'Times cadastrados:\n\n'
    )
    for i, (nome, _) in enumerate(times.items()):
        print(
            f'T-00{i} - Clube: {nome}\n'
        )
    print(
        '\nPressione Enter para voltar:\n'
        'Digite o indice do time que deseja remover:'
    )
    while True:
        escolha = input('>>> T-00').strip()
        if escolha == '':
            limpar_tela()
            print('Voltando ao menu principal...')
            sleep(2)
            limpar_tela()
            break

        elif escolha.isdigit() and not escolha.isalpha():
            indice = int(escolha)

            if 0 <= indice < len(times):
                limpar_tela()
                nome_time = list(times.keys())[indice]
                del times[nome_time]
                print(
                    'Gestão de times de futebol:\n\n'\
                    f'Time {nome_time} removido com sucesso!\n\n'
                )
                sleep(1.2)
                limpar_tela()
                break

            else:
                print(
                    'Time não encontrado...'
                    'Tente novamente...'
                )
                sleep(1)
                limpar_tela()
                remover_time()
        else:
            print('Formato inválido...')
            sleep(2)
            limpar_tela()
            break

def adicionar_jogador():
    if not times:
        print(
            'Gestão de times de futebol:\n\n'
            'Nenhum time cadastrado!\n\n'
            'Voltando ao menu principal...'
        )
        sleep(1.2)
        limpar_tela()
        return

    while True:
        limpar_tela()
        print(
            'Gestão de times de futebol:\n\n'
            'Adicionar jogador:\n'
            'Times cadastrados:\n'
        )
        for i, (nome, _) in enumerate(times.items()):
            print(f'T-00{i} - Clube: {nome}')

        print(
            '\nPressione Enter para voltar.\n'
            'Digite o índice do time que deseja adicionar jogador:'
        )
        escolha = input('>>> T-00').strip()

        if escolha == '':
            limpar_tela()
            print('Voltando ao menu principal...')
            sleep(2)
            limpar_tela()
            break

        if not escolha.isdigit():
            print('Formato inválido. Insira um número válido.')
            sleep(2)
            limpar_tela()
            continue

        indice = int(escolha)
        if 0 <= indice < len(times):
            nome_time = list(times.keys())[indice]
            limpar_tela()
            print(
                f'Gestão de times de futebol:\n\n'
                f'Adicionar jogador ao time "{nome_time}":\n\n'
            )
            while True:
                print('Digite [s]im para adicionar ou [n]ão para cancelar:')
                escolha = input('>>> ').strip().lower()
                if escolha == 's':
                    limpar_tela()
                    print(
                        'Gestão de times de futebol:\n\n'
                        'Digite o nome do jogador:'
                    )
                    novo_jogador = input('>>> ').strip()
                    if novo_jogador and novo_jogador not in times[nome_time]:
                        times[nome_time].append(novo_jogador)
                        print(
                            f'Jogador "{novo_jogador}" adicionado ao time "{nome_time}"!\n'
                        )
                        sleep(2)
                        limpar_tela()
                        break
                    else:
                        print(
                            'Nome inválido ou jogador já cadastrado. Tente novamente.'
                        )
                        sleep(2)
                        limpar_tela()
                elif escolha == 'n':
                    limpar_tela()
                    print('Voltando ao menu principal...')
                    sleep(2)
                    limpar_tela()
                    break
                else:
                    print('Opção inválida. Tente novamente.')
                    sleep(2)
                    limpar_tela()
        else:
            print('Índice não encontrado. Tente novamente.')
            sleep(2)
            limpar_tela()

def remover_jogador():
    if not times:
        print(
            'Gestão de times de futebol:\n\n'
            'Nenhum time cadastrado!\n\n'
            'Voltando ao menu principal...'
        )
        sleep(1.2)
        limpar_tela()
        return
    print(
        'Gestão de jogadores de futebol:\n\n'
        'Remover jogador:\n'
        'Times cadastrados:\n\n'
    )
    for i, (nome_time, j) in enumerate(times.items()):
        print(f'T-00{i} - Clube: {nome_time}')
    
    print(
        '\nPressione Enter para voltar:\n'
        'Digite o índice do time do qual deseja remover um jogador:'
    )
    while True:
        escolha = input('>>> T-00').strip()
        
        if escolha == '':
            limpar_tela()
            print('Voltando ao menu principal...')
            sleep(2)
            limpar_tela()
            break

        elif escolha.isdigit() and not escolha.isalpha():
            indice = int(escolha)
            
            if 0 <= indice < len(times):
                limpar_tela()
                nome_time = list(times.keys())[indice]
                jogadores = times[nome_time]
                
                if not jogadores:
                    limpar_tela()
                    print(f'O time {nome_time} não tem jogadores cadastrados.')
                    sleep(1.5)
                    limpar_tela()
                    break
                
                print(f'\nJogadores do time "{nome_time}":')
                for j, jogador in enumerate(jogadores, 1):
                    print(f'{j} - {jogador}')
                
                print(
                    '\nDigite o número do jogador que deseja remover, ou pressione Enter para voltar:'
                )
                
                escolha_jogador = input('>>> ').strip()
                
                if escolha_jogador == '':
                    limpar_tela()
                    print('Voltando ao menu principal...')
                    sleep(2)
                    limpar_tela()
                    break
                
                if escolha_jogador.isdigit() and 1 <= int(escolha_jogador) <= len(jogadores):
                    jogador_removido = jogadores.pop(int(escolha_jogador) - 1)
                    limpar_tela()
                    print(f'O jogador "{jogador_removido}" foi removido do time "{nome_time}".')
                    sleep(2)
                    limpar_tela()
                    break
                else:
                    limpar_tela()
                    print('Jogador não encontrado, tente novamente...')
                    sleep(1)
                    limpar_tela()
            else:
                print('Time não encontrado... Tente novamente...')
                sleep(1)
                limpar_tela()
                break
        else:
            print('Formato inválido... Tente novamente...')
            sleep(2)
            limpar_tela()
            break

def listar_jogadores_time():
    if not times:
        print(
            'Gestão de jogadores de futebol:\n\n'
            'Nenhum time cadastrado!\n\n'
            'Voltando ao menu principal...'
        )
        sleep(2.5)
        limpar_tela()
        return
    
    print(
        'Gestão de jogadores de futebol:\n\n'
        'Listar jogadores:\n'
        'Times cadastrados:\n\n'
    )
    
    for i, nome_time in enumerate(times.keys()):
        print(f'T-00{i} - Clube: {nome_time}')
    
    print(
        '\nPressione Enter para voltar:\n'
        'Digite o índice do time para listar seus jogadores:'
    )
    
    while True:
        escolha = input('>>> T-00').strip()
        
        if escolha == '':
            limpar_tela()
            print('Voltando ao menu principal...')
            sleep(2)
            limpar_tela()
            break

        elif escolha.isdigit() and not escolha.isalpha():
            indice = int(escolha)
            
            if 0 <= indice < len(times):
                limpar_tela()
                nome_time = list(times.keys())[indice]
                jogadores = times[nome_time]
                
                if not jogadores:
                    limpar_tela()
                    print(f'O time {nome_time} não tem jogadores cadastrados.')
                    sleep(1.5)
                    limpar_tela()
                    break
                
                print(f'\nJogadores do time "{nome_time}":')
                for j, jogador in enumerate(jogadores, 1):
                    print(f'{j} - {jogador}')
                
                print(
                    '\nPressione Enter para voltar:'
                )

                while True:
                    escolha = input('>>> ').strip()
                    if escolha == '':
                        limpar_tela()
                        return

                    else:
                        print('Opção inválida...')
                        sleep(2)
                        limpar_tela()
                        break
            else:
                print('Time não encontrado... Tente novamente...')
                sleep(1)
                limpar_tela()
                break
        else:
            print('Formato inválido... Tente novamente...')
            sleep(2)
            limpar_tela()
            break


def sair():
    exit()

entrada = None
while True:
    menu()
    entrada = input('>>> ')
    if not entrada.isdigit():
        print('Opção inválida...')
        sleep(2)
        limpar_tela()
        continue
    
    if  entrada == '7':
        limpar_tela()
        print(

            'Gestão de times de futebol:\n\n'\
            'Deseja sair?\n\n'
            'Digite [s]im:  Digite [n]ão:'
        )
        while True:
            escolha = input('>>> ')
            if escolha == 's' or escolha == '':
                limpar_tela()
                print('Encerrando...')
                sleep(2)
                sair()
                
            elif escolha == 'n':
                limpar_tela()
                break

            else:
                print('Opção inválida...')
                sleep(2)
                limpar_tela()
                break
        

    elif entrada == '6':
        limpar_tela()
        print(

            'Gestão de times de futebol:\n\n'\
            '0 - Listar jogadores\n'\
            '1 - Voltar\n\n'
            'Digite 0 para listar os jogadores de um time:\n'\
            'Digite 1/Enter para voltar ao menu principal:'
        )
        while True:
            escolha = input('>>> ')

            if escolha == '' or escolha == '1':
                limpar_tela()
                break

            elif escolha == '0':
                limpar_tela()
                listar_jogadores_time()
                break

            else:
                print('Opção inválida...')
                sleep(2)
                limpar_tela()
                break

    elif entrada == '5':
        limpar_tela()
        print(

            'Gestão de times de futebol:\n\n'\
            '0 - Remover jogadores\n'\
            '1 - Voltar\n\n'
            'Digite 0 para remover um jogador:\n'\
            'Digite 1/Enter para voltar ao menu principal:'
        )
        while True:
            escolha = input('>>> ')

            if escolha == '' or escolha == '1':
                limpar_tela()
                break

            elif escolha == '0':
                limpar_tela()
                remover_jogador()
                break

            else:
                print('Opção inválida...')
                sleep(2)
                limpar_tela()
                break

    elif entrada == '4':
        limpar_tela()
        print(

            'Gestão de times de futebol:\n\n'\
            '0 - Adicionar jogadores\n'\
            '1 - Voltar\n\n'
            'Digite 0 para adicionar um jogador:\n'\
            'Digite 1/Enter para voltar ao menu principal:'
        )
        while True:
            escolha = input('>>> ')

            if escolha == '' or escolha == '1':
                limpar_tela()
                break

            elif escolha == '0':
                limpar_tela()
                adicionar_jogador()
                break

            else:
                print('Opção inválida...')
                sleep(2)
                limpar_tela()
                break

    elif entrada == '3':
        limpar_tela()
        print(

            'Gestão de times de futebol:\n\n'\
            '0 - Remover time\n'\
            '1 - Voltar\n\n'
            'Digite 0 para remover um time:\n'\
            'Digite 1/Enter para voltar ao menu principal:'
        )
        while True:
            escolha = input('>>> ')

            if escolha == '' or escolha == '1':
                limpar_tela()
                break

            elif escolha == '0':
                limpar_tela()
                remover_time()
                break

            else:
                print('Opção inválida...')
                sleep(2)
                limpar_tela()
                break

    elif entrada == '2':
        limpar_tela()
        print(

            'Gestão de times de futebol:\n\n'\
            'Adicionar time:\n\n'
            '0 - Continuar\n'\
            '1 - Voltar\n\n'
            'Digite 0 para continuar\n'\
            'Digite 1/Enter para voltar ao menu principal:'
        )
        while True:
            escolha = input('>>> ')

            if escolha == '' or escolha == '1':
                limpar_tela()
                break

            elif escolha == '0':
                limpar_tela()
                adicionar_time()
                break

            else:
                print('Opção inválida...')
                sleep(2)
                limpar_tela()
                break

    elif entrada == '1':
        limpar_tela()
        print(

            'Gestão de times de futebol:\n\n'\
            '0 - Listar times\n'\
            '1 - Voltar\n\n'
            'Digite 0 para ver a lista de times:\n'\
            'Digite 1/Enter para voltar ao menu principal:'
        )
        while True:
            escolha = input('>>> ')

            if escolha == '' or escolha == '1':
                limpar_tela()
                break

            elif escolha == '0':
                limpar_tela()
                listar_times()
                break

            else:
                print('Opção inválida...')
                sleep(2)
                limpar_tela()
                break
            

    else:
        print('Opção inválida...')
        sleep(2)
        limpar_tela()
        continue
