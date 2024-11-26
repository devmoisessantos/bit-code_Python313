# MODULO HASHLIB:

"""
- O modulo hashlib possui diversas funcoes para trabalhar 
com hash
- Ex: criptografia, hash, etc...

É bastante utilizado para trabalhar com dados, por exemplo:

"""

import hashlib

# 1 - TIPOS DE HASH:
print(hashlib.algorithms_available) 
# Todos os algoritmos disponiveis:
'''
{
    'sha224', 'sha3_224', 
    'md5', 'blake2s', 
    'sha512_224', 'sha256', 
    'sha3_512', 'sha3_256', 
    'shake_128', 'sha1', 
    'sha3_384', 'sha384', 
    'blake2b', 'sha512_256', 
    'sm3', 'sha512', 'md5-sha1', 
    'shake_256', 'ripemd160'
 }
'''
print()

print(hashlib.algorithms_guaranteed)
# Todos os algoritmos garantidos Windows:
'''
{
    'blake2s', 'blake2b', 
    'shake_128', 'sha3_224', 
    'sha224', 'sha512', 
    'sha3_512', 'md5', 
    'shake_256', 'sha3_256', 
    'sha1', 'sha384', 
    'sha256', 'sha3_384'
}
'''

# 2 - Hash:
senha = '123456'
hash = hashlib.sha256(senha.encode('utf-8')).hexdigest()
print(f'Hash: {hash}')

# 3 - Verificar se a senha esta correta:
senha_correta = '123456'
hash_correto = hashlib.sha256(senha_correta.encode('utf-8')).hexdigest()

if hash == hash_correto:
    print('Senha correta')
else:
    print('Senha incorreta')

texto = 'Ola, mundo!'   
hash = hashlib.sha256(texto.encode('utf-8')).hexdigest()
print(
    f'Texto: {texto}\n'

    f'Crypt: {hash}\n'
)

