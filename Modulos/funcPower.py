# Agendamento de Desligamento de Computador
import datetime
import time
import os


def funcAgendPowerOff(hora, minuto):
    """
    Agendamento de Desligamento do Computador para uma hora específica.
    """
    print(f"Agendamento de desligamento para as {hora:02}:{minuto:02}.")
    while True:
        now = datetime.datetime.now()
        if now.hour == hora and now.minute == minuto:
            os.system("shutdown /s /t 0")  # Desliga imediatamente
            print(f"Computador desligando às {hora:02}:{minuto:02}.")
            break
        time.sleep(30)  # Verifica a cada 30 segundos para reduzir o uso da CPU

# funcAgendPowerOff()

def funcPowerOff(seconds):
    # Desligamento de Computador
    os.system(f'shutdown /s /t {seconds}') # Desliga o Computador imediatamente

# funcPowerOff()

def funcReboot():
    # Reinicializa o Computador
    os.system("shutdown /r /t 0") # Reinicializa o Computador imediatamente

# funcReboot()

def funcCancelShutdown():
    # Cancela o Desligamento do Computador
    os.system("shutdown /a") # Cancela o Desligamento do Computador

# funcCancelShutdown()