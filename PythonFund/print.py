
# A funcao print() serve para imprimir algo na tela
# Por ser uma funcao utiliza-se pareteses
# Para mostrar textos use aspas simples ou duplas ("" | '')
# Para imprimir mais de uma coisa, basta colocar uma virgula.

print('Hello World')
print('My name is Moisés')
print('Estou aprendendo a linguagem Python!')

'''________________________________________________________'''
print()

# Variaveis:

# Em python, podemos criar variaveis para armazenar informacoes
# para isso basta colocar o nome da variavel seguido do sinal de
# atribuicao '=' seguido da informacao que queremos armazenar.

name = 'Moises'
sobrenome = 'Santos'
age = 26
maior_de_idade = True
altura_metros = 1.65

print(name)
print(sobrenome)
print(age)
print(maior_de_idade)
print(altura_metros)
print()


# Tipos de variaveis:
# Para saber o tipo de uma variavel, podemos utilizar a funcao type()

print(type(name))
print(type(age))
print(type(maior_de_idade))
print(type(altura_metros))
print()


# EXERCICIOS:
# 1. Imprimir as seguintes informacoes:
# 1.1 Nome
print(name)

# 1.2 Sobrenome
print(sobrenome)

# 1.3 Idade
print(age)
print()


# Utilizando o f-string

# 2. Mostrar as seguintes informacoes:
# 2.1 Qual o seu nome completo
print(f'Meu nome completo é {name} {sobrenome}.')

# 2.2 Qual a sua idade
print(f'Minha idade é {age}.')

# 2.3 Qual a sua altura
print(f'Minha altura é {altura_metros} metros.')

# 3. Impima o seguinte texto:
# 3.1 Ola, meu nome é Moisés e tenho 18 anos
print(f'Ola, meu nome é {name} e tenho {age} anos.')

# 4. Imprimir o seguinte texto:
# 4.1 Moro em Goiania, Goias, Brasil
print(f'Moro em Goiania, Goias, Brasil.')

