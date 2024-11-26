# EXERCICIO 7:
# - Contagem regressiva:

'''
Crie um programa que mostre na tela uma contagem regressiva para simular o lancamento de um foguete.
O programa deve contar de 10 ate 0, com uma pausa de 1 segundo entre eles.

- Ao final da contagem sera emitido um "beep" de alarme.

'''

from time import sleep
from playsound import playsound
from threading import Thread


def play_countdown_audio():
    playsound('PythonFund/countdown.mp3')


print('*' * 32)

print(

    'O Foguete vai ser lancado em instantes...'
)

print(
        'Evacuando a área...'
)

sleep(1)

print(

    'Iniciando contagem regressiva...\n\n'
)

sleep(1)

print('*' * 16)


print(

    'INICIANDO EM...\n'
)
sleep(2)
countdown_thread = Thread(target=play_countdown_audio)
countdown_thread.start()

sleep(1.9)

for timer in range(10, -1, -1):
    sleep(1.1)
    print(timer)
    
    if timer == 0:
        playsound('PythonFund/beep.mp3')
        print()
        print('Foguete lancado com sucesso.!')