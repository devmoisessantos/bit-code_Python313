# OS OPERADORES ARITMÉTICOS
# + SOMA
op_soma = 10 + 145
print(op_soma)

# - SUBTRAI
op_subtrai = 718 - 12
print(op_subtrai)

# * MULTIPLICA
op_multiplica = 13 * 15
print(op_multiplica)

# / DIVIDE
op_divide = 11 / 14
print(op_divide)

# // DIVISAO INTEIRA
op_divide_inteira = 19 // 11
print(op_divide_inteira)

# % RESTO DA DIVISAO
op_modulo = 5 % 12
print(op_modulo)

# ** EXPOENCIACAO 
op_exponenciacao = 132 ** 12
print(op_exponenciacao)


"""________________________________________________"""
print('')

# OS OPERADORES RELACIONAIS(COMPARAÇÃO)
#  >
operador_maior = op_divide > op_divide_inteira
print(operador_maior)
#  >=
operador_maior_igual = operador_maior >= op_divide_inteira
print(operador_maior_igual)
#  <
operador_menor = op_divide < op_soma
print(operador_menor)
#  <=
operador_menor_igual = op_divide <= op_divide_inteira
print(operador_menor_igual)
#  ==
operador_de_igualdade = operador_menor_igual == op_divide_inteira
print(operador_de_igualdade)
#  !=
operador_de_diferenca = op_divide != operador_de_igualdade
print(operador_de_diferenca)

"""________________________________________________"""
print('')


# OS OPERADORES LOGICOS
# and 
operador_and = operador_de_igualdade and operador_de_diferenca
print(f'O resultado de {operador_de_igualdade} and {operador_de_diferenca} é {operador_and}') # print(operador_and)

# or
operador_or = op_divide or operador_maior    
print(f'O resultado de {op_divide} or {operador_maior} é {operador_or}') # print(operador_or)

# not
operador_not = not operador_and
print(f'O resultado de not {operador_and} é {operador_not}') # print(operador_not)

"""________________________________________________"""
print('')

# OS OPERADORES DE ATRIBUIÇAO
exemplo = None
print(f'{exemplo} {type(exemplo)}')
# =
exemplo = 1
print(f'{exemplo} {type(exemplo)}') # print(exemplo)

# +=
exemplo += 5
print(f'{exemplo} {type(exemplo)}') # print(exemplo)

# -=
exemplo -= 1
print(f'{exemplo} {type(exemplo)}') # print(exemplo)

# *= 
exemplo *= 2
print(f'{exemplo} {type(exemplo)}') # print(exemplo)

# /= 
exemplo /= 2
print(f'{exemplo} {type(exemplo)}') # print(exemplo)

# //= 
exemplo //= 2
print(f'{exemplo} {type(exemplo)}') # print(exemplo)

# %= 
exemplo %= 1
print(f'{exemplo} {type(exemplo)}') # print(exemplo)

# **=
exemplo **= 2
print(f'{exemplo} {type(exemplo)}') # print(exemplo)

"""________________________________________________"""
print('')

# OS OPERADORES DE MEMBRO
# in 
tupla = (1, 2, 3)
print((3) in tupla)

# not in
tupla_2 = (0, 1, 2, 3, 5)
print((1, 2, 3) not in tupla_2)