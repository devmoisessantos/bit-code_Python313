### Listas:

As listas em Python são estruturas de dados muito versáteis, e a linguagem oferece diversos métodos integrados para manipulá-las. Aqui estão os principais métodos de listas:

---

### **1. Adicionar elementos**

- **`append(x)`**
  Adiciona o elemento `x` ao final da lista.

  ```python
  lista = [1, 2, 3]
  lista.append(4)  # [1, 2, 3, 4]
  ```
- **`extend(iterável)`**
  Adiciona os elementos de um iterável (outra lista, tupla, etc.) à lista atual.

  ```python
  lista = [1, 2]
  lista.extend([3, 4])  # [1, 2, 3, 4]
  ```
- **`insert(indice, x)`**
  Insere o elemento `x` na posição especificada por `indice`.

  ```python
  lista = [1, 2, 4]
  lista.insert(2, 3)  # [1, 2, 3, 4]
  ```

---

### **2. Remover elementos**

- **`remove(x)`**
  Remove a primeira ocorrência de `x` na lista.

  ```python
  lista = [1, 2, 3, 2]
  lista.remove(2)  # [1, 3, 2]
  ```
- **`pop(indice=-1)`**
  Remove e retorna o elemento na posição especificada. Por padrão, remove o último.

  ```python
  lista = [1, 2, 3]
  elemento = lista.pop()  # [1, 2], elemento = 3
  ```
- **`clear()`**
  Remove todos os elementos da lista.

  ```python
  lista = [1, 2, 3]
  lista.clear()  # []
  ```

---

### **3. Consultar elementos**

- **`index(x, inicio=0, fim=len(lista))`**
  Retorna o índice da primeira ocorrência de `x`. Pode especificar o intervalo.

  ```python
  lista = [1, 2, 3, 2]
  posicao = lista.index(2)  # 1
  ```
- **`count(x)`**
  Conta o número de vezes que `x` aparece na lista.

  ```python
  lista = [1, 2, 3, 2]
  ocorrencias = lista.count(2)  # 2
  ```

---

### **4. Ordenar ou inverter**

- **`sort(chave=None, reverso=False)`**
  Ordena a lista em ordem crescente (ou decrescente se `reverso=True`).

  ```python
  lista = [3, 1, 2]
  lista.sort()  # [1, 2, 3]
  ```
- **`reverse()`**
  Inverte a ordem dos elementos na lista.

  ```python
  lista = [1, 2, 3]
  lista.reverse()  # [3, 2, 1]
  ```

---

### **5. Copiar a lista**

- **`copy()`**
  Retorna uma cópia rasa da lista.
  ```python
  lista = [1, 2, 3]
  nova_lista = lista.copy()  # [1, 2, 3]
  ```
