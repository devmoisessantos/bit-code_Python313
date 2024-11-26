import os 

# help('os')        # Retorna Ajuda sobre o módulo

print(os.getcwd() + '\n') # Retorna o caminho da pasta atual

# os.mkdir('novo_diretorio') # Cria um novo diretório

# os.rmdir('novo_diretorio') # Remove um diretório

# os.rename('novo_diretorio', 'novo_diretorio_renomeado')

print(os.listdir()) # Retorna uma lista com os arquivos da pasta

print(os.path.exists('arquivo.txt')) # Verifica se o arquivo existe

print(os.path.isfile('.\modulo-os.py')) # Verifica se o arquivo existe

os.system('cls') # Limpa a tela

# os.system('pause') # Pausa o programa

os.system('ping 127.0.0.1') # Envia um ping para o localhost

print(os.environ.get('USERNAME')) # Retorna o nome do usuário


