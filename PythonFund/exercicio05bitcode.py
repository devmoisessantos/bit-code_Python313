# EXERCICIO 5:
# - Calculo de passagem por distancia:

'''
Crie um programa que pergunte a distancia que um passageiro deseja percorrer em km. 

Calcule o preço da passagem,
cobrando R$0,50 por km para viagens de até 200km
e R$0,45 para viagens mais longas.

'''

print(

    'Preço da passagem: \n' \
    '10km até 200km: R$0,50 por km \n' \
    'acima de 200km: R$0,45 por km\n\n'
)

distancia = input('Digite a distancia a ser percorrida em km: \n>>> ') ; print()

if not distancia.isalnum() or distancia.isspace() or distancia == '' or distancia.isalpha():
    try:
        distancia = float(distancia)
    except: 
        print('Distancia inválida... \n')
        exit()
elif not distancia.isdigit():
    print('Distancia inválida... \n')
    exit()

else:
    distancia = int(distancia)
    
if \
    distancia <= 200 and distancia >= 10:
        cobrar_por_km = 0.50
        preco = distancia * cobrar_por_km
        print(

            f'Distancia a ser calculada {distancia}km \n' \
            f'Preço da passagem: R${cobrar_por_km:.2f} \n' \
            f'Preço total: R${preco:.2f} \n \n'
        )

elif \
    distancia > 200:
        cobrar_por_km = 0.45
        preco = distancia * cobrar_por_km
        print(

            f'Distancia a ser calculada {distancia}km \n' \
            f'Preço da passagem: R${cobrar_por_km:.2f} \n' \
            f'Preço total: R${preco:.2f} \n \n'
        )

else:
    print(

        f'Distancia a ser calculada {distancia}km \n \n' \
        'Não está dentro do intervalo de 10km e 200km \n'\
        '> Passagem nao pode ser calculada... \n \n'

)
