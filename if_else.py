# ESTRUTURA CONDICIONAL IF-ELSE EM PYTHON :

# if condicao:
#     executa se a condicao for verdadeira
# else:
#     executa se a condicao for falsa


name = input("Digite o  nome do jogo? ")
year = int(input("Digite o ano de lançamento do jogo? "))
classification = float(input("Digite a nota de classificação do jogo? "))


if classification >= 8.0 and year >= 2015:
    print("==DADOS DO JOGO==")
    print("Nome do jogo: ", name)
    print("Ano do jogo: ", year)
    print("A classificação do jogo: ", classification,'\n')
    print(f"O jogo {name} é gratuito e muito Bom. Recomendado!")
else:
    print("==DADOS DO JOGO==")
    print("Nome do jogo: ", name)
    print("Ano do jogo: ", year)
    print("A classificação do jogo: ", classification, '\n')
    print(f"O jogo {name} é Ruim. Não recomendo !")
