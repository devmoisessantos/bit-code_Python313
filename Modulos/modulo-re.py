# MODULO RE:
"""
- O modulo re possui diversas funcoes para trabalhar 
com expressões regulares
- Ex: busca, substituição, etc...

É bastante utilizado para trabalhar com texto, por exemplo:

"""

import re


texto = "Python é uma linguagem incrível para aprender e programar."

# Indice inicial e final de palavras
'''
O 'r' significa que queremos que a string seja interpretada
como uma string bruta (raw string)

''' 

# 1 - Buscar a substring "incrivel para aprender"
i = re.search(r'incrível para aprender', texto)

if i:  # Verifica se o padrão foi encontrado
    print('Índice inicial:', i.start())
    print('Índice final:', i.end())
else:
    print('Padrão não encontrado no texto.')

# 2 - Buscando o indice que possui o "."

i = re.search(r'\.', texto)

print(i)


# 3 - Encontrando todos os caracteres de 'a' até 'm'

texto = "Python é uma linguagem incrível para aprender e programar."

# Padrão para encontrar caracteres de 'a' até 'm' (case-sensitive)
padrao = r'[a-m]'

# Usar re.findall para encontrar todos os caracteres correspondentes
resultado = re.findall(padrao, texto)

print(resultado)  # Exibe os caracteres encontrados



# 4 - Verificando o inicio de uma string

# Padrão que verifica se uma string começa com "A"
padrao = r'^A'

# Lista de frases
frases = ['O dia esta lindo', 'Aula de Python', 'String com um padrao']

# Verificar cada frase
for frase in frases:
    if re.match(padrao, frase):  # Verificar se a frase começa com "A"
        print(f'A frase "{frase}" inicia com o padrão.')
    else:
        print(f'A frase "{frase}" não inicia com o padrão.')



# 5 - Buscando uma lista de caracteres dentro de uma string

# Padrão que verifica se uma string termina com "!"
padrao = r'!$'

# String para verificar
frase = 'O dia esta lindo'

# Verificar se a frase termina com "!"
if re.search(padrao, frase):  # Use re.search para o final
    print(f'A frase "{frase}" termina com o padrão.')
else:
    print(f'A frase "{frase}" não termina com o padrão.')
