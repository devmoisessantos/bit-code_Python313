### **`isinstance(object, classinfo)`**
Verifica se um objeto é uma instância de uma classe ou de uma tupla de classes.

- **Parâmetros:**  
  1. `object`: o objeto a ser verificado.  
  2. `classinfo`: uma classe ou tupla de classes.

- **Exemplo:**  
  ```python
  print(isinstance(5, int))  # Saída: True
  print(isinstance(5, (int, float)))  # Saída: True
  print(isinstance("text", int))  # Saída: False
  ```

---

### **`issubclass(class, classinfo)`**
Verifica se uma classe é uma subclasse de outra ou de uma tupla de classes.

- **Parâmetros:**  
  1. `class`: a classe a ser verificada.  
  2. `classinfo`: uma classe ou tupla de classes.

- **Exemplo:**  
  ```python
  class A:
      pass

  class B(A):
      pass

  print(issubclass(B, A))  # Saída: True
  print(issubclass(A, B))  # Saída: False
  ```

---

### **`iter(object[, sentinel])`**
Retorna um iterador para o objeto. Se `sentinel` for fornecido, cria um iterador que chama uma função até o valor `sentinel`.

- **Parâmetros:**  
  1. `object`: um objeto iterável ou chamável.  
  2. `sentinel` (opcional): valor de parada.

- **Exemplo:**  
  ```python
  nums = [1, 2, 3]
  it = iter(nums)
  print(next(it))  # Saída: 1
  print(next(it))  # Saída: 2
  ```

- **Com `sentinel`:**
  ```python
  with open("example.txt") as file:
      for line in iter(file.readline, ''):
          print(line.strip())
  ```

---

### **`len(object)`**
Retorna o número de itens em um objeto.

- **Parâmetro:**  
  `object`: um objeto que suporte comprimento, como listas, strings ou dicionários.

- **Exemplo:**  
  ```python
  print(len([1, 2, 3]))  # Saída: 3
  print(len("Python"))  # Saída: 6
  ```

---

### **`locals()`**
Retorna um dicionário das variáveis locais no momento.

- **Exemplo:**  
  ```python
  def example():
      x = 10
      print(locals())

  example()  # Saída: {'x': 10}
  ```

---

### **`map(function, iterable, ...)`**
Aplica uma função a cada item de um ou mais iteráveis, retornando um iterador.

- **Parâmetros:**  
  1. `function`: a função a ser aplicada.  
  2. `iterable`: um ou mais iteráveis.

- **Exemplo:**  
  ```python
  nums = [1, 2, 3]
  squared = map(lambda x: x ** 2, nums)
  print(list(squared))  # Saída: [1, 4, 9]
  ```

---

### **`max(iterable, *[, key, default])`**
Retorna o maior item em um iterável ou o maior de dois ou mais argumentos.

- **Parâmetros:**  
  1. `iterable`: coleção de elementos.  
  2. `key` (opcional): função para extração de chaves.  
  3. `default` (opcional): valor retornado se o iterável estiver vazio.

- **Exemplo:**  
  ```python
  print(max([1, 2, 3]))  # Saída: 3
  print(max("abc", key=lambda x: ord(x)))  # Saída: 'c'
  ```

---

### **`min(iterable, *[, key, default])`**
Retorna o menor item em um iterável ou o menor de dois ou mais argumentos.

- **Parâmetros:**  
  1. `iterable`: coleção de elementos.  
  2. `key` (opcional): função para extração de chaves.  
  3. `default` (opcional): valor retornado se o iterável estiver vazio.

- **Exemplo:**  
  ```python
  print(min([1, 2, 3]))  # Saída: 1
  print(min("abc", key=lambda x: ord(x)))  # Saída: 'a'
  ```

---

### **`next(iterator[, default])`**
Retorna o próximo item de um iterador. Se o iterador estiver esgotado, retorna o valor `default` (se fornecido) ou lança um erro `StopIteration`.

- **Parâmetros:**  
  1. `iterator`: o iterador.  
  2. `default` (opcional): valor de fallback.

- **Exemplo:**  
  ```python
  it = iter([1, 2, 3])
  print(next(it))  # Saída: 1
  print(next(it))  # Saída: 2
  print(next(it, 'Fim'))  # Saída: 3
  print(next(it, 'Fim'))  # Saída: 'Fim'
  ```

---

### **`object()`**
Retorna uma nova instância de um objeto vazio.

- **Exemplo:**  
  ```python
  obj = object()
  print(obj)  # Saída: <object object at 0x...>
  ```

---

### **`oct(x)`**
Converte um número inteiro em uma string octal prefixada com `0o`.

- **Parâmetro:**  
  `x` (int): o número a ser convertido.

- **Exemplo:**  
  ```python
  print(oct(8))  # Saída: '0o10'
  ```

---

### **`open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)`**
Abre um arquivo e retorna um objeto de arquivo.

- **Parâmetros:**  
  1. `file`: nome ou caminho do arquivo.  
  2. `mode`: modo de abertura ('r', 'w', 'a', etc.).  
  3. Outros parâmetros opcionais.

- **Exemplo:**  
  ```python
  with open("example.txt", "r") as f:
      print(f.read())
  ```

---

### **`ord(c)`**
Retorna o código Unicode de um caractere.

- **Parâmetro:**  
  `c` (str): caractere de um único símbolo.

- **Exemplo:**  
  ```python
  print(ord('a'))  # Saída: 97
  print(ord('€'))  # Saída: 8364
  ```

---
