O módulo **`re`** do Python fornece suporte para **expressões regulares**, permitindo buscar, combinar e manipular padrões em strings.

---

### **Importação do módulo**

```python
import re
```

---

## **Funções principais**

### **1. `re.match(pattern, string, flags=0)`**
Verifica se o padrão **corresponde ao início da string**.

- **Parâmetros:**
  - `pattern`: Padrão da expressão regular.
  - `string`: String onde será feita a busca.
  - `flags`: Modificadores opcionais (como `re.IGNORECASE`).

- **Retorno:** Um objeto `match` ou `None`.

- **Exemplo:**
  ```python
  result = re.match(r'\d+', '123abc')
  print(result.group())  # Saída: '123'
  ```

---

### **2. `re.search(pattern, string, flags=0)`**
Procura pelo padrão **em qualquer posição na string**.

- **Parâmetros:** (iguais a `match`).
- **Retorno:** Um objeto `match` ou `None`.

- **Exemplo:**
  ```python
  result = re.search(r'abc', '123abc456')
  print(result.group())  # Saída: 'abc'
  ```

---

### **3. `re.findall(pattern, string, flags=0)`**
Retorna **uma lista** com todas as ocorrências do padrão na string.

- **Parâmetros:** (iguais a `match`).
- **Retorno:** Uma lista de strings.

- **Exemplo:**
  ```python
  result = re.findall(r'\d+', 'a1b2c3')
  print(result)  # Saída: ['1', '2', '3']
  ```

---

### **4. `re.finditer(pattern, string, flags=0)`**
Retorna um **iterador** de objetos `match` para todas as ocorrências.

- **Parâmetros:** (iguais a `match`).
- **Retorno:** Um iterador.

- **Exemplo:**
  ```python
  for match in re.finditer(r'\d+', 'a1b2c3'):
      print(match.group())  # Saída: '1', '2', '3'
  ```

---

### **5. `re.sub(pattern, repl, string, count=0, flags=0)`**
Substitui todas as ocorrências do padrão por uma string ou função.

- **Parâmetros:**
  - `pattern`: Padrão a ser substituído.
  - `repl`: Substituição (string ou função).
  - `string`: String original.
  - `count`: Número máximo de substituições.

- **Retorno:** A string com as substituições.

- **Exemplo:**
  ```python
  result = re.sub(r'\d', '*', 'a1b2c3')
  print(result)  # Saída: 'a*b*c*'
  ```

---

### **6. `re.split(pattern, string, maxsplit=0, flags=0)`**
Divide a string usando o padrão como delimitador.

- **Parâmetros:**
  - `pattern`: Padrão delimitador.
  - `string`: String a ser dividida.
  - `maxsplit`: Número máximo de divisões.

- **Retorno:** Uma lista de substrings.

- **Exemplo:**
  ```python
  result = re.split(r'\d+', 'a1b2c3')
  print(result)  # Saída: ['a', 'b', 'c', '']
  ```

---

## **Objetos `match`**

Um objeto retornado por funções como `match` ou `search` possui métodos úteis:

- **`.group()`**: Retorna a string combinada.
- **`.start()`**: Índice de início da correspondência.
- **`.end()`**: Índice do final da correspondência.
- **`.span()`**: Uma tupla com os índices de início e fim.

- **Exemplo:**
  ```python
  result = re.search(r'abc', '123abc456')
  print(result.group())  # 'abc'
  print(result.start())  # 3
  print(result.end())    # 6
  print(result.span())   # (3, 6)
  ```

---

## **Modificadores (Flags)**

Os **modificadores** podem alterar o comportamento das expressões regulares:

- `re.IGNORECASE` ou `re.I`: Ignora diferenças de maiúsculas/minúsculas.
- `re.MULTILINE` ou `re.M`: Permite que `^` e `$` funcionem em várias linhas.
- `re.DOTALL` ou `re.S`: Faz `.` corresponder a novas linhas.
- `re.VERBOSE` ou `re.X`: Permite comentários e espaçamento legível.
- `re.ASCII` ou `re.A`: Força correspondência de caracteres ASCII.

- **Exemplo com flag:**
  ```python
  result = re.search(r'abc', 'ABC', re.IGNORECASE)
  print(result.group())  # 'ABC'
  ```

---

## **Principais Metacaracteres**

1. **Pontuação:**
   - `.`: Qualquer caractere (exceto nova linha).
   - `^`: Início da string.
   - `$`: Fim da string.
   - `*`: Zero ou mais repetições.
   - `+`: Uma ou mais repetições.
   - `?`: Zero ou uma repetição.

2. **Conjuntos:**
   - `[abc]`: Qualquer caractere entre `a`, `b` ou `c`.
   - `[^abc]`: Qualquer caractere **exceto** `a`, `b` ou `c`.
   - `[a-z]`: Intervalo de caracteres.

3. **Grupos:**
   - `(abc)`: Grupo capturado.
   - `(?:abc)`: Grupo não capturado.

4. **Escapando:**
   - `\d`: Dígitos (`[0-9]`).
   - `\D`: Não dígitos (`[^0-9]`).
   - `\w`: Caracteres de palavra (`[a-zA-Z0-9_]`).
   - `\W`: Não caracteres de palavra.
   - `\s`: Espaços em branco (`[\t\n\r\f\v]`).
   - `\S`: Não espaços.

---
