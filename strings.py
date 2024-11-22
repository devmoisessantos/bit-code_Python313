# STRINGS:

# Uma string e um conjunto de caracteres.

string_aspas_simples = 'Exemplo com aspas simples'
string_aspas_dupla = "Exemplo com aspas duplas"

exemplo_docstring = """

Exemplo de docstring:

Aqui dentro de uma DocString
Pode ter quantas linhas quiser sem problemas.

"""

print(string_aspas_simples)
print(string_aspas_dupla)
print(exemplo_docstring)
print()

# OPERACOES COM STRINGS

# Concatenacao
name = 'Moises'
sobrenome = 'Santos'
nome_completo = name + ' ' + sobrenome
print(f'{nome_completo} é meu nome completo.')
print()

# Repeticao
print('*' * 14)
print()

# Indexacao
print(name[0])
print(name[:5])
print(name[-1])
print()

# Verificacao
print('s' in name)
print('a' not in sobrenome)
print()

# Formatacao
print(f'{name} tem {len(name)} letras.')    
print()

# Metodos
print(name.upper(), ' --- metodo para tudo maiusculo')
print(name.lower(), ' ---- metodo para tudo minusculo')
print(name.title(), ' ---- metodo para a primeira letra maiuscula')
print(name.replace('s', 'x'),  ' --- metodo para substituir')
print(name.strip(), ' --- metodo para remover espacos')
print(name.split(' '), ' -- metodo para quebrar a string')  
print(name.find('s'), ' ---- metodo para encontrar')
print(name.count('s'), '  --- metodo para contar caracteres')
print(name.isnumeric(), ' ----- metodo para saber se eh numerico')
print(name.isalpha(), ' ----- metodo para saber se eh alfabetico')
print(name.isalnum(), ' --- metodo para saber se eh alfanumerico')
print(name.startswith('M'), ' ------- metodo para saber se comeca com')
print(name.endswith('s'), ' -- metodo para saber se termina com')
print(name.capitalize(), ' -- metodo para deixar a primeira letra maiuscula')
print(name.center(20), ' --- metodo para centralizar')
print(name.ljust(20), ' --- metodo para alinhar a esquerda')
print(name.rjust(20), ' ------ metodo para alinhar a direita')
print(name.zfill(20), ' --- metodo para preencher com zeros')
print(name.encode('utf-8'), ' ----- metodo para converter para bytes')
