def somar(x, y):
    return f'{x} + {y} = {x + y}'

def subtrair(x, y):
    return f'{x} - {y} = {x - y}'

def dividir(x, y):
    if y == 0 or x == 0:
        return 'Não é possivel dividir por 0\n'\
        f'{x} / {y} = Ø'
    return f'{x} / {y} = {x / y}'

def multiplicar(x, y):
    return f'{x} * {y} = {x * y}'