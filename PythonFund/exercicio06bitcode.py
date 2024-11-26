# EXERCICIO 5:
# - Aumentar o salario de funcionario:

'''
Crie um programa que pergunte o salario de um funcionario e
    calcule o valor do seu aumento.

    Para salarios superiores a R$1250,00, calcule um aumento de 10%
    Para inferiores ou iguais, o aumento é de 15% .

'''

print(

    'Aumentar salarios: \n' \
    'Salario ate R$1250,00: aumentar 15% \n' \
    'Salario acima de R$1250,00: aumentar 10%\n\n'
)

entrada_usuario = input('Digite o salario do funcionario: \n>>> ') ; print()

entrada_valida = \
        entrada_usuario.isalnum() \
        or entrada_usuario.isspace() \
        or entrada_usuario == '' \
        or entrada_usuario.isalpha()

salario_atual = None
novo_salario = None

if not \
        entrada_valida:
    try:
        salario_atual = float(entrada_usuario)

    except: 
        print(f'Salario: "{entrada_usuario}" inválido... \n')
        exit()

elif not \
        entrada_usuario.isdigit():
        print(f'Salario: "{entrada_usuario}" inválido... \n')
        exit()

else:
    salario_atual = int(entrada_usuario)


if \
    salario_atual <= 1250 and entrada_usuario > '':
        novo_salario = salario_atual * 1.15
        print(

        f'O salario atual: {salario_atual} \n' \
        f'Foi calculado um aumento de 15% \n' \
        f'O novo salario sera: {novo_salario:.2f} \n'

    )
        
elif \
        salario_atual >= 1250 and entrada_usuario > '':
            novo_salario = salario_atual * 1.10
            print(

        f'O salario atual: {salario_atual} \n' \
        f'Foi calculado um aumento de 10% \n' \
        f'O novo salario sera: {novo_salario:.2f} \n'

    )
            
else:
    print(f'Salario: "{entrada_usuario}" inválido... \n')
