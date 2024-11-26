# MODULO JSON:

# JSON - Javascript Object Notation
"""
É um formato de dados em texto simples para armazenar dados 
estruturados.

"""

import json 

# 1 -  Strings para dicionario:

pessoa_json = '{"nome": "Moises", "idade": 26, "linguagem": "Python"}'

pessoa_dict = json.loads(pessoa_json)
print(pessoa_dict, '\n')
print(pessoa_dict['linguagem'],'\n\n')

# 2 - Dicionario para Json:

dicionario_json = {
    "nome": "Moises", 
    "idade": 26, 
    "linguagem": "Python"
}

json_string = json.dumps(dicionario_json)
print(json_string)
print(type(json_string))
print(type(dicionario_json), '\n\n')

# 3 - Formatando o Json:

dicionario_json = {
    "nome": "Moises", 
    "idade": 26, 
    "linguagem": "Python"
}

json_string = json.dumps(dicionario_json, indent=4, sort_keys=True)
print(json_string, '\n\n')

# 4 - Salvando Json em TXT:

dicionario_json = {
    "nome": "Moises", 
    "idade": 26, 
    "linguagem": "Python"
}

with open('Modulos/pessoa_json.txt', 'w') as f:
    json.dump(dicionario_json, f)
print('Json salvo com sucesso!', '\n\n')

# 5 - Lendo Json externo:

with open('Modulos/iris.json', 'r') as file:
    data = json.load(file)
print(data, '\n\n')
