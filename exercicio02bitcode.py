'''
EXERCICIO 2:

Média de quatro(4) notas:
--> Escreva um programa em Python que leia quatro
numeros e nos devolva a média entre esses numeros. 
Utilize os operadores aritimeticos.


pseudo_code:
Início
    Mostrar mensagem "Digite a primeira nota:"
    Ler nota1
    Mostrar mensagem "Digite a segunda nota:"
    Ler nota2
    Mostrar mensagem "Digite a terceira nota:"
    Ler nota3
    Mostrar mensagem "Digite a quarta nota:"
    Ler nota4

    Somar as quatro notas e armazenar em soma
    Calcular a média dividindo soma por 4 e armazenar em media

    Mostrar a média calculada
Fim

'''
cabecalho = ('*' * 16) + '\n' + 'CALCULAR MÉDIA\n' + ('*' * 16)
print(cabecalho)

print('Digite a primeira nota: ')
nota_num1 = float(input('>>> '))
print(f'{nota_num1} \n')


print('Digite a segunda nota: ')
nota_num2 = float(input('>>> '))
print(f'{nota_num2} \n')


print('Digite a terceira nota: ')
nota_num3 = float(input('>>> '))
print(f'{nota_num3} \n')


print('Digite a quarta nota: ')
nota_num4 = float(input('>>> '))
print(f'{nota_num4} \n')


somar_notas = (
    nota_num1 +
    nota_num2 +
    nota_num3 +
    nota_num4
)

media_notas = somar_notas / 4

print(f'A média das notas digitadas é: {media_notas:.1f}')
