# MODULO STATISTIC:

"""
- O modulo statistic possui diversas funcoes estatisticas
- Ex: media, mediana, moda, desvio padrao, etc...

É bastante utilizado para trabalhar com dados, por exemplo:

"""

from statistics import *

# 1 - Media:
media = mean([1, 2, 3, 4, 5])
print(
    f'Media: {media}' 
)

# 2 - Mediana:
mediana = median([1, 2, 3, 4, 5])
mediana_ = median([1, 2, 3, 4, 5, 6])
print(
    f'Mediana: {mediana}\n'
    f'Mediana: {mediana_}'
)

# 3 - Moda:
moda = mode([1, 2, 3, 4, 5, 2, 2, 7, 8, 1, 3, 9, 0, 3, 6])
print(
    f'Moda: {moda}' 
)

# 4 - Desvio Padrao:
"""
- Quanto mais próximo de zero, mais homogeneo os dados.
- Quanto mais próximo de 1, mais heterogeneo os dados.
"""
print(
    f'Desvio Padrao: {stdev([1.3, 2, 2.5, 3, 3.1, 4.9, 5.2], xbar=None):.2f}'
)
