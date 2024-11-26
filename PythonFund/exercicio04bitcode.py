# Exercício 4:

'''
Subistituindo caracteres especificos:
--> Escreva um programa em Python para substituir os dois primmeiros caracteres 
especificos de uma string pelos dois ultimos de outra. Ex: 'banana' -> 'cebola' = banola | cebana.



pseudo_code:
1. Receber duas string de entrada.
2. Se as string não estiver vazia:
   a. Obter a primeira string.
   b. Obter a segunda string de entrada.
   c. Substituir as duas ocorrências desse primeiro string pela da outra'.
   d. Substituir as duas ocorrências desse segundo string pela da primeira'.
3. Exibir a nova string modificada.

'''

str1 = 'xyz'
str2 = 'abc'
nova_str = str1[0:2] + str2[2:]
print(nova_str)
nova_str2 = str2[0:2] + str1[2:]
print(nova_str2)



# primeira_string = input("Digite a primeira string: ")
# segunda_string = input("Digite a segunda string: ")

# if len(primeira_string) > 0 and len(segunda_string) > 0:
#     primeira_string = primeira_string[0:2]
#     segunda_string = segunda_string[2:]
#     nova_string = primeira_string + segunda_string
#     print(nova_string)
# else:
#     print(primeira_string)


# primeira_string = primeira_string
# segunda_string = segunda_string
# resultado = substituir_caracteres_especificos(primeira_string, segunda_string)
# print(resultado)




# primeira_string = input("Digite a primeira string: ")
# segunda_string = input("Digite a segunda string: ")
# primeira_string = primeira_string
# segunda_string = segunda_string
# resultado = substituir_caracteres_especificos(segunda_string, primeira_string)
# print(resultado)