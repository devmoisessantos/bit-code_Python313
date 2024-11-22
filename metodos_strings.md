### Métodos de Strings em Python

1. **`str.capitalize()`**

   - **Descrição**: Retorna uma cópia da string com o primeiro caractere em maiúsculo e o restante em minúsculo.
   - **Exemplo**:
     ```python
     "hello".capitalize()  # 'Hello'
     ```
2. **`str.casefold()`**

   - **Descrição**: Retorna uma cópia da string com todos os caracteres em minúsculo (mais agressivo que `lower()`).
   - **Exemplo**:
     ```python
     "HELLO".casefold()  # 'hello'
     ```
3. **`str.center(width, fillchar=' ')`**

   - **Descrição**: Retorna uma string centrada, preenchendo os espaços extras com o caractere `fillchar`.
   - **Exemplo**:
     ```python
     "hello".center(10, '-')  # '--hello---'
     ```
4. **`str.count(substring, start=0, end=len(string))`**

   - **Descrição**: Conta quantas vezes o `substring` aparece na string entre os índices `start` e `end`.
   - **Exemplo**:
     ```python
     "hello world".count("o")  # 2
     ```
5. **`str.encode(encoding='utf-8', errors='strict')`**

   - **Descrição**: Retorna uma versão codificada da string em um formato de bytes, usando o tipo de codificação especificado.
   - **Exemplo**:
     ```python
     "hello".encode()  # b'hello'
     ```
6. **`str.endswith(suffix, start=0, end=len(string))`**

   - **Descrição**: Retorna `True` se a string terminar com o sufixo especificado, caso contrário retorna `False`.
   - **Exemplo**:
     ```python
     "hello".endswith("lo")  # True
     ```
7. **`str.expandtabs(tabsize=8)`**

   - **Descrição**: Substitui os caracteres de tabulação (`\t`) na string pelo número de espaços definidos em `tabsize`.
   - **Exemplo**:
     ```python
     "hello\tworld".expandtabs(4)  # 'hello   world'
     ```
8. **`str.find(substring, start=0, end=len(string))`**

   - **Descrição**: Retorna o índice da primeira ocorrência de `substring`. Retorna `-1` se não encontrado.
   - **Exemplo**:
     ```python
     "hello".find("e")  # 1
     ```
9. **`str.format(*args, **kwargs)`**

   - **Descrição**: Formata a string, substituindo os espaços reservados por valores.
   - **Exemplo**:
     ```python
     "Hello, {}!".format("world")  # 'Hello, world!'
     ```
10. **`str.index(substring, start=0, end=len(string))`**

    - **Descrição**: Retorna o índice da primeira ocorrência de `substring`. Levanta uma exceção `ValueError` se não encontrado.
    - **Exemplo**:
      ```python
      "hello".index("e")  # 1
      ```
11. **`str.isalnum()`**

    - **Descrição**: Retorna `True` se todos os caracteres na string forem alfanuméricos (letras e números), caso contrário `False`.
    - **Exemplo**:
      ```python
      "hello123".isalnum()  # True
      ```
12. **`str.isalpha()`**

    - **Descrição**: Retorna `True` se todos os caracteres forem letras (a-z, A-Z).
    - **Exemplo**:
      ```python
      "hello".isalpha()  # True
      ```
13. **`str.isdigit()`**

    - **Descrição**: Retorna `True` se todos os caracteres forem dígitos.
    - **Exemplo**:
      ```python
      "12345".isdigit()  # True
      ```
14. **`str.islower()`**

    - **Descrição**: Retorna `True` se todos os caracteres forem minúsculos.
    - **Exemplo**:
      ```python
      "hello".islower()  # True
      ```
15. **`str.isupper()`**

    - **Descrição**: Retorna `True` se todos os caracteres forem maiúsculos.
    - **Exemplo**:
      ```python
      "HELLO".isupper()  # True
      ```
16. **`str.join(iterable)`**

    - **Descrição**: Junta os elementos de um iterável (como uma lista) usando a string como delimitador.
    - **Exemplo**:
      ```python
      "-".join(["a", "b", "c"])  # 'a-b-c'
      ```
17. **`str.lstrip(chars=None)`**

    - **Descrição**: Retorna uma cópia da string com os caracteres iniciais removidos (se fornecido, remove os caracteres em `chars`).
    - **Exemplo**:
      ```python
      "  hello  ".lstrip()  # 'hello  '
      ```
18. **`str.lower()`**

    - **Descrição**: Retorna uma cópia da string com todos os caracteres em minúsculo.
    - **Exemplo**:
      ```python
      "HELLO".lower()  # 'hello'
      ```
19. **`str.lstrip(chars)`**

    - **Descrição**: Remove todos os caracteres à esquerda da string até encontrar um caractere não pertencente ao conjunto especificado em `chars`.
    - **Exemplo**:
      ```python
      "!!!hello".lstrip("!")  # 'hello'
      ```
20. **`str.replace(old, new, count=-1)`**

    - **Descrição**: Retorna uma nova string onde todas as ocorrências de `old` são substituídas por `new`, até um máximo de `count` vezes.
    - **Exemplo**:
      ```python
      "hello world".replace("world", "Python")  # 'hello Python'
      ```
21. **`str.rfind(substring, start=0, end=len(string))`**

    - **Descrição**: Retorna o índice da última ocorrência de `substring`. Retorna `-1` se não encontrado.
    - **Exemplo**:
      ```python
      "hello".rfind("l")  # 3
      ```
22. **`str.rstrip(chars=None)`**

    - **Descrição**: Retorna uma cópia da string com os caracteres finais removidos (se fornecido, remove os caracteres em `chars`).
    - **Exemplo**:
      ```python
      "hello   ".rstrip()  # 'hello'
      ```
23. **`str.split(sep=None, maxsplit=-1)`**

    - **Descrição**: Divide a string em uma lista de substrings. Por padrão, usa qualquer espaço em branco como delimitador.
    - **Exemplo**:
      ```python
      "hello world".split()  # ['hello', 'world']
      ```
24. **`str.startswith(prefix, start=0, end=len(string))`**

    - **Descrição**: Retorna `True` se a string começar com o prefixo fornecido.
    - **Exemplo**:
      ```python
      "hello".startswith("he")  # True
      ```
25. **`str.strip(chars=None)`**

    - **Descrição**: Remove os caracteres à esquerda e à direita da string.
    - **Exemplo**:
      ```python
      "  hello  ".strip()  # 'hello'
      ```
26. **`str.title()`**

    - **Descrição**: Retorna uma versão da string com cada palavra começando com uma letra maiúscula.
    - **Exemplo**:
      ```python
      "hello world".title()  # 'Hello World'
      ```
27. **`str.upper()`**

    - **Descrição**: Retorna uma cópia da string com todos os caracteres em maiúsculo.
    - **Exemplo**:
      ```python
      "hello".upper()  # 'HELLO'
      ```
28. **`str.zfill(width)`**

    - **Descrição**: Preenche a string com zeros à esquerda até atingir o comprimento especificado por `width`.
    - **Exemplo**:
      ```python
      "42".zfill(5)  # '00042'
      ```
