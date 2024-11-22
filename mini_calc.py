numero_um = None
operador = None
numero_dois = None
'''
___________________
'''
resultado = None

if \
    operador is None:
    numero_um = input('Digite o primeiro numero: ')
    operador = input('Qual operador? +, -, *, /, %, **: ')
    numero_dois = input('Digite o segundo numero: ')
    

    if \
        operador == '+':
            resultado = float(numero_um) + float(numero_dois)
            print(f'{numero_um} + {numero_dois} = {resultado}')

    elif \
            operador == '-':
            resultado = float(numero_um) - float(numero_dois)
            print(f'{numero_um} - {numero_dois} = {resultado}')

    elif \
            operador == '*':    
            resultado = float(numero_um) * float(numero_dois)
            print(f'{numero_um} * {numero_dois} = {resultado}')

    elif \
            operador == '/':
            resultado = float(numero_um) / float(numero_dois)
            print(f'{numero_um} / {numero_dois} = {resultado}')

    elif \
            operador == '%':
            resultado = float(numero_um) % float(numero_dois)
            print(f'{numero_um} % {numero_dois} = {resultado}')

    elif \
            operador == '**':
            resultado = float(numero_um) ** float(numero_dois)
            print(f'{numero_um} ** {numero_dois} = {resultado}')

else:
    print('Digite um operador valido: \n(+ - * / % **)')      

