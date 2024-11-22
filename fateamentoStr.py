'''
Fateamento de Strings:

O Slice serve para extrair partes de uma string.

Sintaxe:

minha_string[inicio:fim:passo]

O inicio e o fim devem ser inteiros e o passo pode ser opcional.
'''


veiculo = 'Bicicleta'

print(veiculo[:], ' -------- Imprime a string completa') # Imprime a string completa 
print(veiculo[0:3], ' ----- Imprime a string de 0 a 3 (caracteres)') # 'Imprime a string de 0 a 3 (caracteres)'
print(veiculo[0::2], ' ---- Imprime a string de 0(caractere) ao fim pulando de 2 em 2') # 'Imprime a string de 0(caractere) ao fim pulando de 2 em 2'
print(veiculo[::-1], ' ------- Imprime a string ao contrario') # 'Imprime a string ao contrario'
print(veiculo[-1], ' ------- Imprime o ultimo caractere') # 'Imprime o ultimo caractere'


