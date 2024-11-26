# FUNCOES :
"""
- Uma funcao em python eh um bloco de codigo que realiza uma tarefa especifica.
- Pode ou nao receber argumentos de entrada e retornar um valor de saida.

Usadas para repetir determinados blocos de codigo sem a necessidade de criar um novo escopo.

___________________________________________________________________________________

# Sintaxe de uma funcao:

def nome_funcao(parametros):
    bloco de instrucoes
    return valor_de_retorno

___________________________________________________________________________________

"""

# Exemplos:

def saudacao():
    print('Bom dia!')

saudacao()


# FUNCOES COM INPUT():

# Exemplos:

def saudacao():
    nome = input('Qual o seu nome? ')
    print(f'Bom dia {nome}!')

saudacao()

