'''
EXERCICIO 3:

Subistituindo caracteres repetidos:
--> Escreva um programa em Python para obter uma string de uma determinada palavra.
Todas as ocorrencias de seu primeiro caractere foram alteraddos para '$', 
exceto o primeiro caractere. Ex: 'banana' -> 'b$nn$'.


pseudo_code:
1. Receber uma string de entrada.
2. Se a string não estiver vazia:
   a. Obter o primeiro caractere da string.
   b. Substituir todas as ocorrências desse primeiro caractere (exceto a primeira) por '$'.
3. Exibir a nova string modificada.

'''


input_palavra = input("Digite uma palavra: ")
"""
Recebe uma string e retorna uma nova string com todas as ocorrências do 
primeiro caractere substituídas por '$', exceto o primeiro caractere.

:param: palavra: str
:return: str
"""
def substituir_caracteres_repetidos(palavra):

    
    if len(palavra) > 0:
        primeiro_caractere = palavra[0]
        nova_palavra = primeiro_caractere
        
        for char in palavra[1:]:
            if char == primeiro_caractere:
                nova_palavra += '$' 
            else:
                nova_palavra += char 
        return nova_palavra
    else:
        return palavra 

palavra = input_palavra
resultado = substituir_caracteres_repetidos(palavra)
print(resultado)

input_palavra



'''______________________________________________________________'''
print()

