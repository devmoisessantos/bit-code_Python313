# DICIONARIOS:

# Um dicionario em Python eh uma estrutura de dados que permite armazenar e manipular uma colecao de pares chave-valor.
# Os dicionarios em Python podem ser criados usando chaves {} ou a funcao dict().
'''
_____________________________________________________________________________________'''

# Criando um dicionario vazio:
dicionario_vazio = {}
dicio_vazio = dict()

# Criando um dicionario com elementos:
dicionario = {
        'nome': 'Moises',
        'idade': 26,
        'cidade': 'Goianira',
        'estado': 'Goias',
        'pais': 'Brasil'
}

# Acessando elementos do dicionario:
for chave, valor in dicionario.items():
    print(f'{chave}: {valor}')

# Verificando se uma chave pertence ao dicionario:
if 'nome' in dicionario:
    print('A chave "nome" pertence ao dicionario.')

# Verificando se uma chave nao pertence ao dicionario:
if 'endereco' not in dicionario:
    print('A chave "endereco" nao pertence ao dicionario.')

# Adicionando elementos ao dicionario:
dicionario['endereco'] = {
    'Rua':'NG-03',
    'Quadra':'05',
    'Lote':'27'
}

print(dicionario)

# Removendo elementos do dicionario:
del dicionario['endereco']
print(dicionario)

# Copiando um dicionario:
dicionario_copia = dicionario.copy()
print(dicionario_copia)

# Limpar um dicionario:
dicionario.clear()
print(dicionario)

