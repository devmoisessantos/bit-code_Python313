### **`eval(expression, globals=None, locals=None)`**
Avalia uma expressão Python fornecida como string e retorna o resultado.

- **Parâmetros:**  
  1. `expression` (str): a expressão a ser avaliada.  
  2. `globals` (opcional): dicionário de variáveis globais.  
  3. `locals` (opcional): dicionário de variáveis locais.

- **Exemplo:**  
  ```python
  x = 10
  print(eval("x + 5"))  # Saída: 15
  ```

---

### **`exec(object, globals=None, locals=None)`**
Executa código Python fornecido como string ou objeto compilado.

- **Parâmetros:**  
  1. `object` (str ou código compilado): código a ser executado.  
  2. `globals` (opcional): dicionário de variáveis globais.  
  3. `locals` (opcional): dicionário de variáveis locais.

- **Exemplo:**  
  ```python
  code = "for i in range(3): print(i)"
  exec(code)  # Saída: 0, 1, 2
  ```

---

### **`filter(function, iterable)`**
Retorna um iterador contendo os elementos do iterável para os quais a função retorna `True`.

- **Parâmetros:**  
  1. `function` (função): função de teste.  
  2. `iterable` (iterável): coleção de elementos.

- **Exemplo:**  
  ```python
  nums = [1, 2, 3, 4]
  even = filter(lambda x: x % 2 == 0, nums)
  print(list(even))  # Saída: [2, 4]
  ```

---

### **`float([x])`**
Converte um valor para tipo `float`.

- **Parâmetro:**  
  `x` (opcional): valor a ser convertido.

- **Exemplo:**  
  ```python
  print(float(5))  # Saída: 5.0
  print(float("3.14"))  # Saída: 3.14
  ```

---

### **`format(value, format_spec)`**
Formata um valor usando a especificação de formato fornecida.

- **Parâmetros:**  
  1. `value`: valor a ser formatado.  
  2. `format_spec` (str): especificação de formato.

- **Exemplo:**  
  ```python
  print(format(1234.567, ".2f"))  # Saída: '1234.57'
  print(format(255, "x"))  # Saída: 'ff'
  ```

---

### **`getattr(object, name[, default])`**
Retorna o valor de um atributo de um objeto.

- **Parâmetros:**  
  1. `object`: o objeto a ser inspecionado.  
  2. `name` (str): nome do atributo.  
  3. `default` (opcional): valor retornado se o atributo não existir.

- **Exemplo:**  
  ```python
  class MyClass:
      x = 10

  obj = MyClass()
  print(getattr(obj, 'x'))  # Saída: 10
  print(getattr(obj, 'y', 'Not Found'))  # Saída: 'Not Found'
  ```

---

### **`globals()`**
Retorna um dicionário das variáveis globais atuais.

- **Exemplo:**  
  ```python
  x = 10
  print(globals())  # Inclui 'x' no dicionário
  ```

---

### **`hasattr(object, name)`**
Verifica se um objeto tem um atributo com o nome especificado.

- **Parâmetros:**  
  1. `object`: o objeto a ser inspecionado.  
  2. `name` (str): nome do atributo.

- **Exemplo:**  
  ```python
  class MyClass:
      x = 10

  obj = MyClass()
  print(hasattr(obj, 'x'))  # Saída: True
  print(hasattr(obj, 'y'))  # Saída: False
  ```

---

### **`hash(object)`**
Retorna o valor do hash de um objeto.

- **Parâmetro:**  
  `object`: qualquer objeto hashable.

- **Exemplo:**  
  ```python
  print(hash("abc"))  # Saída: valor hash (varia)
  ```

---

### **`help([object])`**
Exibe a documentação de um objeto ou ajuda geral sobre o Python.

- **Parâmetro:**  
  `object` (opcional): objeto sobre o qual buscar ajuda.

- **Exemplo:**  
  ```python
  help(str)  # Exibe a documentação da classe `str`
  ```

---

### **`hex(x)`**
Converte um número inteiro em uma string hexadecimal prefixada com `0x`.

- **Parâmetro:**  
  `x` (int): o número a ser convertido.

- **Exemplo:**  
  ```python
  print(hex(255))  # Saída: '0xff'
  ```

---

### **`id(object)`**
Retorna o identificador único de um objeto (endereço na memória).

- **Parâmetro:**  
  `object`: o objeto a ser inspecionado.

- **Exemplo:**  
  ```python
  x = 42
  print(id(x))  # Saída: identificador do objeto
  ```

---

### **`input([prompt])`**
Lê uma linha de entrada do usuário.

- **Parâmetro:**  
  `prompt` (opcional): texto exibido ao usuário.

- **Exemplo:**  
  ```python
  name = input("Qual é o seu nome? ")
  print(f"Olá, {name}!")
  ```

---

### **`int([x], [base])`**
Converte um valor para tipo inteiro.

- **Parâmetros:**  
  1. `x` (opcional): valor a ser convertido.  
  2. `base` (opcional): base numérica para conversão.

- **Exemplo:**  
  ```python
  print(int("1010", 2))  # Saída: 10
  print(int(3.14))  # Saída: 3
  ```

---
