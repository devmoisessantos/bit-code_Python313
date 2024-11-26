# DICIONARIOS ANINHADOS:
'''
- Um dicionario aninhado nada mais é do que um\varios dicionarios dentro de um dicionario.

'''
import pprint

dicionario = {

   '_aninhado' : {
       'nome': 'Moises',
       'idade': 26
   },

    'endereco': {
        'rua': 'Av. Brasil',
        'numero': 123,
        'bairro': 'Centro',
        'cidade': 'Goiania',
        'estado': 'Goias',
        'pais': 'Brasil'
    }, 

    'telefone': {
        'principal': '123456789',
        'celular': '987654321'

    },

    'email': {
        'principal': 'k2H5K@example.com',
        'secundario': 'HgY3o@example.com'

    },  

    'aniversario': {
        'dia': 15,
        'mes': 8,
        'ano': 2000
    }
}
for chave, valor in dicionario.items():
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(f'Chave: {chave} - Valor: {valor} - Tipo: {type(valor)}') #pp.pprint(chave) 