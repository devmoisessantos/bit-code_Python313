O módulo `builtins` do Python contém todas as funções, exceções e objetos fundamentais que estão disponíveis por padrão no ambiente Python, sem a necessidade de importar explicitamente. Abaixo, segue um resumo do `builtins` com alguns exemplos de uso:

---

### Funções do módulo `builtins`

#### Funções Comuns
1. **`abs(x)`**  
   Retorna o valor absoluto de um número.
   ```python
   print(abs(-10))  # Saída: 10
   ```

2. **`all(iterable)`**  
   Retorna `True` se todos os elementos de um iterável forem verdadeiros.
   ```python
   print(all([True, 1, "Hello"]))  # Saída: True
   print(all([True, 0, "Hello"]))  # Saída: False
   ```

3. **`any(iterable)`**  
   Retorna `True` se pelo menos um elemento do iterável for verdadeiro.
   ```python
   print(any([False, 0, ""]))  # Saída: False
   print(any([False, 1, ""]))  # Saída: True
   ```

4. **`bin(x)`**  
   Converte um número inteiro para uma string representando seu valor binário.
   ```python
   print(bin(10))  # Saída: '0b1010'
   ```

5. **`bool(x)`**  
   Converte um valor para seu equivalente booleano.
   ```python
   print(bool(0))  # Saída: False
   print(bool(1))  # Saída: True
   ```

6. **`enumerate(iterable, start=0)`**  
   Retorna um iterador que produz tuplas contendo um índice e o elemento correspondente do iterável.
   ```python
   lista = ['a', 'b', 'c']
   for i, valor in enumerate(lista, start=1):
       print(i, valor)
   # Saída:
   # 1 a
   # 2 b
   # 3 c
   ```

7. **`filter(function, iterable)`**  
   Filtra elementos de um iterável com base em uma função.
   ```python
   nums = [1, 2, 3, 4, 5]
   pares = filter(lambda x: x % 2 == 0, nums)
   print(list(pares))  # Saída: [2, 4]
   ```

8. **`map(function, iterable)`**  
   Aplica uma função a todos os elementos de um iterável.
   ```python
   nums = [1, 2, 3]
   quadrados = map(lambda x: x ** 2, nums)
   print(list(quadrados))  # Saída: [1, 4, 9]
   ```

9. **`max(iterable, *[, key, default])` e `min(iterable, *[, key, default])`**  
   Retorna o maior/menor elemento do iterável.
   ```python
   nums = [1, 2, 3]
   print(max(nums))  # Saída: 3
   print(min(nums))  # Saída: 1
   ```

10. **`zip(*iterables)`**  
    Combina elementos de vários iteráveis em tuplas.
    ```python
    a = [1, 2, 3]
    b = ['a', 'b', 'c']
    print(list(zip(a, b)))  # Saída: [(1, 'a'), (2, 'b'), (3, 'c')]
    ```

---

### Outras Funções Importantes
- **`print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)`**  
  Exibe os objetos na saída padrão.
- **`input([prompt])`**  
  Lê uma entrada do usuário.
- **`len(s)`**  
  Retorna o tamanho de um objeto.
- **`sorted(iterable, key=None, reverse=False)`**  
  Retorna uma lista ordenada a partir de um iterável.
- **`sum(iterable, start=0)`**  
  Retorna a soma dos elementos no iterável.

---

### Exceções e Classes Fundamentais
O módulo `builtins` também contém exceções e classes essenciais como:
- **`Exception`, `ValueError`, `TypeError`, `KeyError`, `IndexError`**  
  Lidam com erros e exceções.
- **`int`, `float`, `str`, `list`, `dict`, `set`, `tuple`**  
  Classes fundamentais para tipos de dados básicos.

```python
try:
    x = int("abc")
except ValueError as e:
    print("Erro:", e)
# Saída: Erro: invalid literal for int() with base 10: 'abc'
```

---

### Listando todos os objetos em `builtins`
Você pode listar todos os objetos disponíveis no módulo `builtins`:
```python
import builtins

print(dir(builtins))
```
