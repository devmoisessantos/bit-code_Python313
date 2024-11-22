Em Python, o tipo de dado **`set`** (conjunto) é uma coleção desordenada e mutável que não permite elementos duplicados. Ele é útil para operações que envolvem lógica de conjuntos como união, interseção, diferença, etc.

Aqui estão os principais métodos disponíveis para conjuntos (`set`) em Python:

---

### **1. Adição e Remoção de Elementos**
- **`add(element)`**  
  Adiciona um elemento ao conjunto. Se o elemento já existir, nada acontece.  
  ```python
  s = {1, 2, 3}
  s.add(4)  # {1, 2, 3, 4}
  ```

- **`remove(element)`**  
  Remove um elemento específico do conjunto. Lança um erro (`KeyError`) se o elemento não existir.  
  ```python
  s = {1, 2, 3}
  s.remove(2)  # {1, 3}
  ```

- **`discard(element)`**  
  Remove um elemento, se ele existir. Caso contrário, não faz nada (não lança erro).  
  ```python
  s = {1, 2, 3}
  s.discard(4)  # {1, 2, 3}
  ```

- **`pop()`**  
  Remove e retorna um elemento arbitrário do conjunto. Lança erro se o conjunto estiver vazio.  
  ```python
  s = {1, 2, 3}
  elem = s.pop()  # elem pode ser 1, 2 ou 3
  ```

- **`clear()`**  
  Remove todos os elementos do conjunto.  
  ```python
  s = {1, 2, 3}
  s.clear()  # set()
  ```

---

### **2. Operações de Conjuntos**
- **`union(other_set)`**  
  Retorna a união do conjunto atual com outro. Não altera o conjunto original.  
  ```python
  s1 = {1, 2}
  s2 = {2, 3}
  s1.union(s2)  # {1, 2, 3}
  ```

- **`intersection(other_set)`**  
  Retorna a interseção dos conjuntos.  
  ```python
  s1 = {1, 2, 3}
  s2 = {2, 3, 4}
  s1.intersection(s2)  # {2, 3}
  ```

- **`difference(other_set)`**  
  Retorna os elementos que estão no conjunto atual, mas não no outro.  
  ```python
  s1 = {1, 2, 3}
  s2 = {2, 3, 4}
  s1.difference(s2)  # {1}
  ```

- **`symmetric_difference(other_set)`**  
  Retorna os elementos que estão em um dos conjuntos, mas não em ambos.  
  ```python
  s1 = {1, 2, 3}
  s2 = {2, 3, 4}
  s1.symmetric_difference(s2)  # {1, 4}
  ```

---

### **3. Operações em Conjunto Mutáveis**
- **`update(other_set)`**  
  Atualiza o conjunto com a união de si mesmo e do outro.  
  ```python
  s1 = {1, 2}
  s2 = {2, 3}
  s1.update(s2)  # s1 agora é {1, 2, 3}
  ```

- **`intersection_update(other_set)`**  
  Atualiza o conjunto com a interseção.  
  ```python
  s1 = {1, 2, 3}
  s2 = {2, 3, 4}
  s1.intersection_update(s2)  # s1 agora é {2, 3}
  ```

- **`difference_update(other_set)`**  
  Atualiza o conjunto removendo os elementos que estão no outro conjunto.  
  ```python
  s1 = {1, 2, 3}
  s2 = {2, 3, 4}
  s1.difference_update(s2)  # s1 agora é {1}
  ```

- **`symmetric_difference_update(other_set)`**  
  Atualiza o conjunto com a diferença simétrica.  
  ```python
  s1 = {1, 2, 3}
  s2 = {2, 3, 4}
  s1.symmetric_difference_update(s2)  # s1 agora é {1, 4}
  ```

---

### **4. Métodos de Consulta**
- **`issubset(other_set)`**  
  Verifica se todos os elementos do conjunto estão contidos no outro.  
  ```python
  s1 = {1, 2}
  s2 = {1, 2, 3}
  s1.issubset(s2)  # True
  ```

- **`issuperset(other_set)`**  
  Verifica se o conjunto atual contém todos os elementos do outro.  
  ```python
  s1 = {1, 2, 3}
  s2 = {2, 3}
  s1.issuperset(s2)  # True
  ```

- **`isdisjoint(other_set)`**  
  Verifica se dois conjuntos não têm elementos em comum.  
  ```python
  s1 = {1, 2}
  s2 = {3, 4}
  s1.isdisjoint(s2)  # True
  ```

---

### **5. Outros Métodos**
- **`copy()`**  
  Retorna uma cópia rasa do conjunto.  
  ```python
  s = {1, 2, 3}
  s_copy = s.copy()  # {1, 2, 3}
  ```

---

### **Exemplo Completo**
```python
s1 = {1, 2, 3}
s2 = {3, 4, 5}

# União
print(s1.union(s2))  # {1, 2, 3, 4, 5}

# Interseção
print(s1.intersection(s2))  # {3}

# Diferença
print(s1.difference(s2))  # {1, 2}

# Atualização com união
s1.update(s2)
print(s1)  # {1, 2, 3, 4, 5}
```

