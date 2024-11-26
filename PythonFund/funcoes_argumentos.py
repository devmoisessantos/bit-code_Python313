# FUNCOES COM ARGUMENTOS:
"""
As funcoes podem receber argumentos, vejamos como fazer isso:

"""

def saudacao(nome):
    print(f'Bom dia {nome}!')

saudacao('Moises')

def saudacao(nome, sobrenome):
    print(f'Bom dia {nome} {sobrenome}!')

saudacao('Moises', 'M Santos')

# Exemplos de funcoes com retorno:

def soma(a, b):
    return a + b

print(soma(2, 3))

# Exemplos de funcoes com argumentos variaveis:

def soma(*args):
    return sum(args)

print(soma(2, 3, 4, 5))

# Exemplos de funcoes com argumentos nomeados:

def soma(**kwargs):
    return sum(kwargs.values())

print(soma(a=2, b=3, c=4, d=5))

# Exemplos de funcoes com argumentos padrao:

def soma(a=0, b=0):
    return a + b

print(soma())
print(soma(2, 3))

"""
Consulta um CEP e retorna os dados de endereço, se o CEP for válido.

:param cep: O CEP a ser consultado, pode ser informado com ou sem hifens.
:type cep: str
:return: Um dicionário com os dados de endereço, se o CEP for válido.
:rtype: dict or None
"""
import requests

def consultar_cep(cep):

    cep = cep.replace('-', '')

    if len(cep) != 8:
        print('CEP inválido!')
    
    url = f'https://viacep.com.br/ws/{cep}/json/'

    try:
        dados = requests.get(url).json()
    except:
        print('CEP não encontrado!')
        return None

    print(

        f'CEP informado válido: \n\n'
        f'Rua: {dados["logradouro"]}\n'
        f'Bairro: {dados["bairro"]}\n'
        f'Cidade: {dados["localidade"]}\n'
        f'Viacep: {dados["cep"]}'
    )

cep = input('Digite um CEP: ')
consultar_cep(cep)