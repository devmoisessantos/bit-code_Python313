'''
EXERCICIO 1:

Antecessor e Sucessor de um numero:
--> Escreva um programa em Python que leia um
numero e nos devolva o numero antecessor e o sucessor
do numero digitado. Utilize os operadores aritimeticos.



pseudo_code:
1. Pegar um numero/letra aleatorio do usuario
2. Identificar o antecessor e o sucessor
3. Imprimir o antecessor e o sucessor

'''
antecessor = None
sucessor = None

letras = [
    'a', 'b', 'c', 'd',
      'e', 'f', 'g', 'h',
        'i', 'j', 'k', 'l',
          'm', 'n', 'o', 'p',
            'q', 'r', 's', 't',
              'u', 'v', 'w', 'x',
                'y', 'z'
    ]

entrada = input('Digite um numero: ')

if entrada.isdigit():
    entrada = int(entrada)
    antecessor = entrada - 1
    sucessor = entrada + 1
    print(
        f'Antecessor ({antecessor}) <- {entrada} -> ({sucessor}) Sucessor '
    )

elif entrada.isalpha():
    entrada = entrada.lower()
    print(f'Você digitou uma letra: {entrada}')
    if entrada in letras:
        antecessor = letras.index(entrada) - 1
        sucessor = letras.index(entrada) + 1
        if entrada == 'a' or letras[antecessor] == 'a':
            antecessor = ' '
            print(
            f'Antecessor ( ) <- {entrada} -> ({letras[sucessor]}) Sucessor '
        )
            
        elif entrada == 'z' or letras[sucessor] == 'z':
            sucessor = ' '
            print(
                f'Antecessor ({letras[antecessor]}) <- {entrada} -> ( ) Sucessor '
            )

        else:
            print(
                f'Antecessor ({letras[antecessor]}) <- {entrada} -> ({letras[sucessor]}) Sucessor '
            )
        
else:
    print('<Erro> Salvo somente numeros e letras válidos.!' )
