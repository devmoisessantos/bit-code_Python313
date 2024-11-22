### Tuplas:

Em Python, tuplas são estruturas de dados imutáveis que permitem armazenar uma coleção de itens. Embora tuplas sejam imutáveis (não podem ser alteradas após serem criadas), Python oferece diversos métodos e operações úteis para trabalhar com elas. Aqui estão os métodos e operações principais:

### 1. **Métodos de tupla**

As tuplas possuem dois métodos principais:

- **`count()`**
  Retorna o número de ocorrências de um elemento específico na tupla.

  ```python
  tupla = (1, 2, 3, 2, 4, 2)
  print(tupla.count(2))  # Saída: 3
  ```
- **`index()`**
  Retorna o índice da primeira ocorrência de um elemento específico. Se o elemento não existir, um erro será levantado.

  ```python
  tupla = (1, 2, 3, 2, 4, 2)
  print(tupla.index(2))  # Saída: 1
  ```

### 2. **Funções úteis que podem ser usadas com tuplas**

- **`len()`**
  Retorna o número de itens na tupla.

  ```python
  tupla = (1, 2, 3)
  print(len(tupla))  # Saída: 3
  ```
- **`max()`**
  Retorna o maior elemento da tupla.

  ```python
  tupla = (1, 2, 3)
  print(max(tupla))  # Saída: 3
  ```
- **`min()`**
  Retorna o menor elemento da tupla.

  ```python
  tupla = (1, 2, 3)
  print(min(tupla))  # Saída: 1
  ```
- **`sum()`**
  Retorna a soma de todos os elementos da tupla (se os elementos forem numéricos).

  ```python
  tupla = (1, 2, 3)
  print(sum(tupla))  # Saída: 6
  ```
- **`sorted()`**
  Retorna uma lista ordenada dos elementos da tupla, sem modificar a tupla original.

  ```python
  tupla = (3, 1, 2)
  print(sorted(tupla))  # Saída: [1, 2, 3]
  ```

### 3. **Operações comuns com tuplas**

- **Acessar elementos por índice**
  Você pode acessar elementos diretamente usando índices.

  ```python
  tupla = (1, 2, 3)
  print(tupla[0])  # Saída: 1
  ```
- **Fatiamento (slicing)**
  Permite acessar um subconjunto dos elementos.

  ```python
  tupla = (1, 2, 3, 4, 5)
  print(tupla[1:4])  # Saída: (2, 3, 4)
  ```
- **Concatenar tuplas**
  É possível concatenar duas ou mais tuplas usando o operador `+`.

  ```python
  tupla1 = (1, 2)
  tupla2 = (3, 4)
  print(tupla1 + tupla2)  # Saída: (1, 2, 3, 4)
  ```
- **Repetir tuplas**
  Multiplicar uma tupla por um inteiro cria uma nova tupla repetida.

  ```python
  tupla = (1, 2)
  print(tupla * 3)  # Saída: (1, 2, 1, 2, 1, 2)
  ```
- **Verificar a existência de um elemento**
  Use o operador `in` para verificar se um elemento está presente na tupla.

  ```python
  tupla = (1, 2, 3)
  print(2 in tupla)  # Saída: True
  ```
- **Iteração com `for`**
  Você pode percorrer os elementos de uma tupla usando um laço `for`.

  ```python
  tupla = (1, 2, 3)
  for item in tupla:
      print(item)
  ```

### 4. **Desempacotamento**

Desempacotamento é atribuir os valores da tupla diretamente a variáveis.

```python
tupla = (1, 2, 3)
a, b, c = tupla
print(a, b, c)  # Saída: 1 2 3
```

### 5. **Conversão entre tupla e lista**

Para modificar elementos, você pode converter uma tupla em lista, alterá-la e convertê-la de volta.

```python
tupla = (1, 2, 3)
lista = list(tupla)
lista.append(4)
tupla = tuple(lista)
print(tupla)  # Saída: (1, 2, 3, 4)
```

