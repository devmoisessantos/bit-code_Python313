# MODULOS:

"""
- O que é um módulo?
Um módulo é um arquivo .py que contém um conjunto de funções relacionadas.

Podemos reutilizar desses módulos suas funcionalidades.

- Como importar um módulo?

        import <modulo>
        from <modulo> import <funcion>
        from <modulo> import *

"""

from calculadora import *


print(
    f'A soma de 2 e 102: {somar(2, 102)}\n\n'
    f'Usando a função para subtrair: {subtrair(102, 2)}\n\n'
    f'A multiplicação de 14 e 3: {multiplicar(14, 3)}\n\n'
    f'A divisão de 15 por 3: {dividir(15, 3)}\n\n'
    f'Tentativa de dividir 16 por 0: {dividir(16, 0)}'
)





