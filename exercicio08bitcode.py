# EXERCICIO 8:
# - Tabuada:

'''
Crie um programa que mostre na tela uma tabuada, o usuario deve informar um numero.
O programa deve fazer a tabuada de numero "x" à numero "y", com o operador que o usuario escolher.

- Ao final sera exibida na tela a Tabuada do numero escolhido.

'''

print(
    'Tabuada: \n' \
    'Operadores disponiveis: \n\n'
    '1 - Adicao (+)\n'
    '2 - Subtracao (-)\n'
    '3 - Divisao (/)\n'
    '4 - Multiplicacao (*)\n' 
    '\n'

    'Selecione um operador: '
    
)

simbolos = {
    '1': '+', '2': '-', '3': '/', '4': '*',
    '+': '+', '-': '-', '/': '/', '*': '*'
}

nomes_operadores = {
    '1': 'Adição', '2': 'Subtração', '3': 'Divisão', '4': 'Multiplicação',
    '+': 'Adição', '-': 'Subtração', '/': 'Divisão', '*': 'Multiplicação'
}



operador = input('>>> ') ; print()
escolha_valida = operador in simbolos


while operador not in simbolos:
    print('Operador invalido! Tente novamente.')
    operador = input('>>> ') ; print()

    
x = int(input('Digite o numero que começara a tabuada: ')) ; print()
numero = int(input('Digite o numero para calcular a tabuada: ')) ; print()
y = int(input('Digite o numero que finalizara a tabuada: ')) ; print()

simbolo = simbolos[operador]
nome_operador = nomes_operadores[operador]

print(
    f"Tabuada: {numero} com o operador de '{nome_operador}':\n"
)

for i in range(x, y + 1):
    
    if operador == '1' or operador == '+':
        resultado = numero + i

    elif operador == '2' or operador == '-':
        resultado = numero - i

    elif operador == '3' or operador == '/':
        resultado = numero / i if i != 0 else "Indefinido (divisão por zero)"

    elif operador == '4' or operador == '*':
        resultado = numero * i

    print(f"{numero} {simbolo} {i} = {resultado}")
    print()
    