# SET | CONJUNTO:
'''
- Um conjunto em Python é uma estrutura de dados que permite armazenar e manipular uma coleção de elementos.
    Conjuntos sao mutáveis, ou seja, podem ser modificadas depois de criadas.
- SET em Python podem ser criadas usando colchetes {}.
Alem disso, também podem ser criadas usando a funcao set().'''

# Criando um conjunto vazio:
conjunto_vazio = set()
set_vazio = {}

# Criando um conjunto com elementos:
conjunto_com_elementos = {1, 2.0, 'Python', True, (1, 2, 3), (4, 5, 6)}

# Acessando elementos do conjunto:
for elemento in conjunto_com_elementos:
    print(elemento)

# Verificando se um elemento pertence ao conjunto:
if 'Python' in conjunto_com_elementos:
    print('O elemento "Python" pertence ao conjunto.')

# Verificando se um elemento nao pertence ao conjunto:
if 'Java' not in conjunto_com_elementos:
    print('O elemento "Java" nao pertence ao conjunto.')

# Adicionando elementos ao conjunto:
conjunto_com_elementos.add('Java')
conjunto_com_elementos.add('C++')
print(conjunto_com_elementos)

# Removendo elementos do conjunto:
conjunto_com_elementos.remove('Java')
print(conjunto_com_elementos)

# Copiando um conjunto:
conjunto_copia = conjunto_com_elementos.copy()
print(conjunto_copia)

# Unindo dois conjuntos:
conjunto1 = {1, 2, 3}
conjunto2 = {4, 5, 6}
conjunto_uniao = conjunto1.union(conjunto2)
print(conjunto_uniao)

# Interseccao de conjuntos:
conjunto_interseccao = conjunto1.intersection(conjunto2)
print(conjunto_interseccao)

# Diferenca de conjuntos:
conjunto_diferenca = conjunto1.difference(conjunto2)
print(conjunto_diferenca)

# Diferenca simetrica de conjuntos:
conjunto_diferenca_simetrica = conjunto1.symmetric_difference(conjunto2)
print(conjunto_diferenca_simetrica)

# Subconjunto de conjuntos:
conjunto_subconjunto = conjunto1.issubset(conjunto2)
print(conjunto_subconjunto)

# Superconjunto de conjuntos:
conjunto_superconjunto = conjunto1.issuperset(conjunto2)
print(conjunto_superconjunto)

# Tamanho de um conjunto:
tamanho_conjunto = len(conjunto_com_elementos)
print(tamanho_conjunto)

# # Excluindo um conjunto:    
# del conjunto_com_elementos
# print(conjunto_com_elementos)

# Limpar um conjunto:
conjunto_com_elementos.clear()
print(conjunto_com_elementos)