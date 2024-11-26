### **`type(object)`**
Retorna o tipo do objeto, ou cria uma nova classe dinâmica.

- **Parâmetros:**  
  1. `object`: o objeto cujo tipo será retornado.  

Quando usado com 3 argumentos, cria uma nova classe.

- **Exemplo:**  
  **Verificando o tipo de um objeto:**  
  ```python
  print(type(5))  # Saída: <class 'int'>
  print(type("Python"))  # Saída: <class 'str'>
  ```

  **Criando uma classe dinâmica:**  
  ```python
  MyClass = type('MyClass', (object,), {'x': 10})
  obj = MyClass()
  print(obj.x)  # Saída: 10
  ```

---

### **`vars([object])`**
Retorna o dicionário de atributos de um objeto. Se nenhum argumento for passado, retorna o dicionário das variáveis locais.

- **Parâmetro:**  
  `object` (opcional): o objeto cujo dicionário de atributos será retornado.

- **Exemplo:**  
  ```python
  class MyClass:
      def __init__(self):
          self.x = 10
          self.y = 20

  obj = MyClass()
  print(vars(obj))  # Saída: {'x': 10, 'y': 20}
  print(vars())  # Retorna as variáveis locais
  ```

---

### **`zip(*iterables)`**
Combina elementos de iteráveis em tuplas, parando no menor comprimento.

- **Parâmetros:**  
  1. `*iterables`: iteráveis a serem combinados.

- **Exemplo:**  
  ```python
  a = [1, 2, 3]
  b = ['a', 'b', 'c']
  print(list(zip(a, b)))  # Saída: [(1, 'a'), (2, 'b'), (3, 'c')]

  # Descompactar com zip
  c = zip(a, b)
  print(list(zip(*c)))  # Saída: [(1, 2, 3), ('a', 'b', 'c')]
  ```

---

### Documentação finalizada!
Todos os métodos solicitados foram documentados com exemplos. 🚀

Se desejar, posso salvar esta documentação como um arquivo para facilitar o uso. Informe o formato desejado, como **PDF** ou **TXT**.