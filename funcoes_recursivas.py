# Funcoes recursivas:
"""
- Funcoes que se chamam a si mesmas, podem ser divididas por partes menores e assim sucessivamente.

- Exemplos:
- Funcao que retorna o fatorial de um numero:
    - 5! = 5 * 4 * 3 * 2 * 1
    - 0! = 1
"""
# Exemplo:

def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)

print(f'O fatorial de 5 e: {fatorial(5)}')

# Exemplo 2:
"""
- Funcao que retorna o fibonacci de um numero:
    - Fibbonacci é uma sequencia de numeros onde o proximo numero eh a soma dos dois anteriores.
    """
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f'O fibonacci de 10 e: {fibonacci(10)}')



