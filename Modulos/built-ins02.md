### **`bin(x)`**
Converte um número inteiro em sua representação binária como uma string prefixada com `0b`.

- **Parâmetro:**  
  `x` (int): o número a ser convertido.

- **Exemplo:**  
  ```python
  print(bin(10))  # Saída: '0b1010'
  print(bin(-10))  # Saída: '-0b1010'
  ```

---

### **`bool([x])`**
Converte um valor em um tipo booleano (`True` ou `False`).

- **Parâmetro:**  
  `x` (opcional): qualquer objeto. Retorna `False` para valores como `None`, `False`, `0`, `[]`, etc.

- **Exemplo:**  
  ```python
  print(bool(0))  # Saída: False
  print(bool([1, 2, 3]))  # Saída: True
  ```

---

### **`breakpoint()`**
Inicia o depurador no ponto em que é chamado.

- **Exemplo:**  
  ```python
  x = 10
  breakpoint()  # Depurador será ativado aqui
  print(x)
  ```

- **Nota:**  
  Usado principalmente para depuração. Substitui o uso direto de `import pdb; pdb.set_trace()`.

---

### **`callable(object)`**
Retorna `True` se o objeto for chamável (como funções ou métodos).

- **Parâmetro:**  
  `object` (qualquer): o objeto a ser verificado.

- **Exemplo:**  
  ```python
  print(callable(print))  # Saída: True
  print(callable(42))  # Saída: False
  ```

---

### **`chr(i)`**
Retorna o caractere Unicode correspondente ao número inteiro.

- **Parâmetro:**  
  `i` (int): valor Unicode.

- **Exemplo:**  
  ```python
  print(chr(97))  # Saída: 'a'
  print(chr(8364))  # Saída: '€'
  ```

---

### **`classmethod(function)`**
Converte um método em um método de classe.

- **Parâmetro:**  
  `function` (função): função a ser convertida.

- **Exemplo:**  
  ```python
  class MyClass:
      @classmethod
      def greet(cls):
          return f"Hello from {cls.__name__}!"

  print(MyClass.greet())  # Saída: 'Hello from MyClass!'
  ```

---

### **`compile(source, filename, mode)`**
Compila o código-fonte em um objeto que pode ser executado.

- **Parâmetros:**  
  1. `source` (str): código Python.
  2. `filename` (str): nome do arquivo associado (para mensagens de erro).
  3. `mode` (str): 'exec', 'eval' ou 'single'.

- **Exemplo:**  
  ```python
  code = compile('print(2 + 3)', '<string>', 'exec')
  exec(code)  # Saída: 5
  ```

---

### **`complex([real[, imag]])`**
Cria um número complexo.

- **Parâmetros:**  
  1. `real` (opcional): parte real (default: 0).  
  2. `imag` (opcional): parte imaginária (default: 0).

- **Exemplo:**  
  ```python
  print(complex(2, 3))  # Saída: (2+3j)
  print(complex(4))  # Saída: (4+0j)
  ```

---

### **`delattr(object, name)`**
Remove o atributo especificado de um objeto.

- **Parâmetros:**  
  1. `object` (objeto): objeto do qual o atributo será removido.  
  2. `name` (str): nome do atributo.

- **Exemplo:**  
  ```python
  class MyClass:
      x = 10

  obj = MyClass()
  delattr(obj, 'x')
  ```

---

### **`dir([object])`**
Retorna a lista de atributos válidos para o objeto.

- **Parâmetro:**  
  `object` (opcional): o objeto a ser inspecionado.

- **Exemplo:**  
  ```python
  print(dir(str))  # Saída: lista de métodos da classe `str`
  ```

---

### **`divmod(a, b)`**
Retorna o quociente e o restante da divisão como uma tupla.

- **Parâmetros:**  
  1. `a` (int ou float): o dividendo.  
  2. `b` (int ou float): o divisor.

- **Exemplo:**  
  ```python
  print(divmod(10, 3))  # Saída: (3, 1)
  ```

---

### **`enumerate(iterable, start=0)`**
Retorna um objeto enumerado, contendo pares (índice, valor).

- **Parâmetros:**  
  1. `iterable`: objeto iterável.  
  2. `start` (opcional): índice inicial (default: 0).

- **Exemplo:**  
  ```python
  for index, value in enumerate(['a', 'b'], start=1):
      print(index, value)
  # Saída: 1 a
  #        2 b
  ```

---

