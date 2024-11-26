# TUPLAS:

# Uma tupla em Python é uma estrutura de dados que permite armazenar e manipular uma coleção de elementos.
# As tuplas em Python podem ser criadas usando parenteses (), alem disso podem ser criadas usando a funcao tuple().

# - Nao são mutaveis, ou seja, nao podem ser modificadas depois de criadas.
# Nao possibilita adicionar ou remover elementos.
# Podem ser indexadas, mas nao podem ser fatiadas.

# Criando uma tupla vazia:
tupla_vazia = ()

# Criando uma tupla com elementos:
tupla_com_elementos = (1, 2.0, 'Python',
                        True, [1, 2, 3], (4, 5, 6))

# Acessando elementos da tupla:
for indice in tupla_com_elementos:
    print(indice)