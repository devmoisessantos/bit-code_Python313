### **`pow(base, exp[, mod])`**
Retorna o valor de \( \text{base}^{\text{exp}} \), opcionalmente calculado módulo `mod`.

- **Parâmetros:**  
  1. `base`: número base.  
  2. `exp`: expoente.  
  3. `mod` (opcional): se fornecido, calcula o resultado módulo `mod`.

- **Exemplo:**  
  ```python
  print(pow(2, 3))  # Saída: 8
  print(pow(2, 3, 5))  # Saída: 3 (8 % 5)
  ```

---

### **`print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)`**
Exibe objetos no console ou em um arquivo.

- **Parâmetros:**  
  1. `*objects`: objetos a serem exibidos.  
  2. `sep` (opcional): separador entre os objetos.  
  3. `end` (opcional): string adicionada no final.  
  4. `file` (opcional): onde imprimir (padrão: console).  
  5. `flush` (opcional): força a limpeza do buffer.

- **Exemplo:**  
  ```python
  print("Olá", "Mundo", sep=", ", end="!\n")  # Saída: Olá, Mundo!
  ```

---

### **`property(fget=None, fset=None, fdel=None, doc=None)`**
Cria um atributo gerenciado em uma classe.

- **Parâmetros:**  
  1. `fget` (opcional): função para obter o valor.  
  2. `fset` (opcional): função para definir o valor.  
  3. `fdel` (opcional): função para deletar o valor.  
  4. `doc` (opcional): documentação.

- **Exemplo:**  
  ```python
  class MyClass:
      def __init__(self):
          self._x = 0

      @property
      def x(self):
          return self._x

      @x.setter
      def x(self, value):
          self._x = value

  obj = MyClass()
  obj.x = 10
  print(obj.x)  # Saída: 10
  ```

---

### **`repr(object)`**
Retorna uma representação de string de um objeto que pode ser usada no `eval()` para recriar o objeto.

- **Parâmetro:**  
  `object`: objeto a ser representado.

- **Exemplo:**  
  ```python
  print(repr("Python"))  # Saída: "'Python'"
  print(repr(3.14))  # Saída: '3.14'
  ```

---

### **`reversed(seq)`**
Retorna um iterador que produz os elementos de uma sequência na ordem inversa.

- **Parâmetro:**  
  `seq`: sequência suportando acesso por índice ou implementando o método `__reversed__`.

- **Exemplo:**  
  ```python
  nums = [1, 2, 3]
  rev = reversed(nums)
  print(list(rev))  # Saída: [3, 2, 1]
  ```

---

### **`round(number[, ndigits])`**
Arredonda um número para um número especificado de dígitos decimais.

- **Parâmetros:**  
  1. `number`: número a ser arredondado.  
  2. `ndigits` (opcional): número de casas decimais.

- **Exemplo:**  
  ```python
  print(round(3.14159, 2))  # Saída: 3.14
  print(round(3.5))  # Saída: 4
  ```

---

### **`setattr(object, name, value)`**
Define o valor de um atributo de um objeto.

- **Parâmetros:**  
  1. `object`: o objeto a ser modificado.  
  2. `name` (str): nome do atributo.  
  3. `value`: valor a ser atribuído.

- **Exemplo:**  
  ```python
  class MyClass:
      pass

  obj = MyClass()
  setattr(obj, 'x', 10)
  print(obj.x)  # Saída: 10
  ```

---

### **`slice(stop)`** ou **`slice(start, stop[, step])`**
Retorna um objeto slice que pode ser usado para fatiar sequências.

- **Parâmetros:**  
  1. `start` (opcional): índice inicial.  
  2. `stop`: índice final.  
  3. `step` (opcional): passo.

- **Exemplo:**  
  ```python
  nums = [0, 1, 2, 3, 4]
  s = slice(1, 4, 2)
  print(nums[s])  # Saída: [1, 3]
  ```

---

### **`sorted(iterable, *, key=None, reverse=False)`**
Retorna uma nova lista com os elementos do iterável ordenados.

- **Parâmetros:**  
  1. `iterable`: coleção de elementos.  
  2. `key` (opcional): função de ordenação.  
  3. `reverse` (opcional): ordena na ordem decrescente.

- **Exemplo:**  
  ```python
  nums = [3, 1, 2]
  print(sorted(nums))  # Saída: [1, 2, 3]
  print(sorted(nums, reverse=True))  # Saída: [3, 2, 1]
  ```

---

### **`staticmethod(function)`**
Converte uma função em um método estático, que não exige instância da classe.

- **Parâmetro:**  
  `function`: função a ser convertida.

- **Exemplo:**  
  ```python
  class MyClass:
      @staticmethod
      def greet():
          return "Olá!"

  print(MyClass.greet())  # Saída: 'Olá!'
  ```

---

### **`sum(iterable, start=0)`**
Soma os itens de um iterável, iniciando com o valor especificado.

- **Parâmetros:**  
  1. `iterable`: coleção de elementos numéricos.  
  2. `start` (opcional): valor inicial.

- **Exemplo:**  
  ```python
  nums = [1, 2, 3]
  print(sum(nums))  # Saída: 6
  print(sum(nums, 10))  # Saída: 16
  ```

---

### **`super([type[, object-or-type]])`**
Retorna um objeto proxy para a classe pai de uma classe.

- **Parâmetros:**  
  1. `type` (opcional): classe atual.  
  2. `object-or-type` (opcional): objeto ou classe para o proxy.

- **Exemplo:**  
  ```python
  class Parent:
      def greet(self):
          return "Olá do Pai!"

  class Child(Parent):
      def greet(self):
          return super().greet() + " E do Filho!"

  print(Child().greet())  # Saída: 'Olá do Pai! E do Filho!'
  ```

---
