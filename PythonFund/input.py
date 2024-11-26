# A funcao input() serve para receber informacoes do usuario
# Assim como a funcao print(), utiliza-se pareteses
# Para mostrar textos use aspas simples ou duplas ("" | '')

# Utilizando a função input():

name_game = input('Qual o nome do jogo? \n')
year_game = int(input('Qual o ano do jogo? \n'))
price_game = input('Qual o preco do jogo? \n')
plan_included = input('Qual o plano do jogo? \n')

# Concatenacao:

print('==DADOS DO JOGO==')
print('=================')
print()

# FORMAS DE CONCATENAR STRINGS

# FORMA 1:
print(
    'Bem vindo ao jogo: ' + name_game
)

# FORMA 2:
print(
    f'O jogo foi lancado em: {year_game}'
)

# FORMA 3:
print(
    'O jogo custa: {}'.format(
        price_game
  )
)

# FORMA 4:
print(
    'O plano do jogo é: %s' % plan_included
)




