Os dicionários em Python possuem diversos métodos úteis para manipulação, consulta e atualização. Aqui estão os principais:

### 1. **Adicionar e Atualizar Itens**
- **`update()`**: Atualiza o dicionário com outro dicionário ou um conjunto de pares chave-valor.
  ```python
  d = {'a': 1}
  d.update({'b': 2, 'c': 3})
  print(d)  # {'a': 1, 'b': 2, 'c': 3}
  ```

### 2. **Acessar Valores**
- **`get()`**: Retorna o valor de uma chave, ou um valor padrão se a chave não existir.
  ```python
  d = {'a': 1}
  print(d.get('a'))  # 1
  print(d.get('b', 'Not Found'))  # Not Found
  ```

### 3. **Remover Itens**
- **`pop()`**: Remove uma chave e retorna seu valor.
  ```python
  d = {'a': 1, 'b': 2}
  print(d.pop('a'))  # 1
  print(d)  # {'b': 2}
  ```

- **`popitem()`**: Remove e retorna o último par chave-valor (em versões mais antigas, era aleatório).
  ```python
  d = {'a': 1, 'b': 2}
  print(d.popitem())  # ('b', 2)
  ```

- **`clear()`**: Remove todos os itens do dicionário.
  ```python
  d = {'a': 1}
  d.clear()
  print(d)  # {}
  ```

### 4. **Consultas**
- **`keys()`**: Retorna uma `view` com todas as chaves.
  ```python
  d = {'a': 1, 'b': 2}
  print(d.keys())  # dict_keys(['a', 'b'])
  ```

- **`values()`**: Retorna uma `view` com todos os valores.
  ```python
  print(d.values())  # dict_values([1, 2])
  ```

- **`items()`**: Retorna uma `view` com todos os pares chave-valor.
  ```python
  print(d.items())  # dict_items([('a', 1), ('b', 2)])
  ```

### 5. **Outros Métodos**
- **`setdefault()`**: Retorna o valor de uma chave, ou insere a chave com um valor padrão.
  ```python
  d = {'a': 1}
  d.setdefault('b', 2)
  print(d)  # {'a': 1, 'b': 2}
  ```

- **`copy()`**: Retorna uma cópia superficial do dicionário.
  ```python
  d = {'a': 1}
  d_copy = d.copy()
  print(d_copy)  # {'a': 1}
  ```

- **`fromkeys()`**: Cria um novo dicionário com chaves fornecidas e um valor padrão.
  ```python
  keys = ['a', 'b']
  d = dict.fromkeys(keys, 0)
  print(d)  # {'a': 0, 'b': 0}
  ```

- **`len()`**: Não é um método, mas retorna o número de itens no dicionário.
  ```python
  d = {'a': 1, 'b': 2}
  print(len(d))  # 2
  ```

### Exemplo Geral:
```python
d = {
    'name': 'Alice',
     'age': 25
}
d.update({'city': 'New York'})  # Adiciona 'city'
print(d.get('age'))            # 25
print(d.keys())                # dict_keys(['name', 'age', 'city'])
d.pop('age')                   # Remove 'age'
print(d)                       # {'name': 'Alice', 'city': 'New York'}
```