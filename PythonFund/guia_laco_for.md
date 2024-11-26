
---

## **Laço `for` em Python**

O laço `for` é usado para iterar sobre uma sequência (como listas, tuplas, strings, dicionários, conjuntos ou até mesmo objetos iteráveis como ranges e geradores). Ele permite executar um bloco de código para cada item na sequência.

### **Sintaxe Básica**

```python
for variável in sequência:
    # Bloco de código
```

- **`variável`**: Recebe o valor do item atual da sequência em cada iteração.
- **`sequência`**: Pode ser qualquer objeto iterável, como uma lista, tupla, string, dicionário ou um objeto que implemente o protocolo iterador.

### **Exemplos Básicos**

#### Iterando por uma lista
```python
frutas = ['maçã', 'banana', 'cereja']
for fruta in frutas:
    print(fruta)
```

#### Iterando por uma string
```python
for letra in "Python":
    print(letra)
```

#### Usando `range`
```python
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)
```

#### Iterando com índices
```python
cores = ['vermelho', 'verde', 'azul']
for i in range(len(cores)):
    print(f'Índice {i}: {cores[i]}')
```

---

## **Função `range()`**

A função `range()` é frequentemente usada com `for` para criar sequências numéricas. Sua sintaxe é:

```python
range(start, stop, step)
```

- `start`: (opcional) Início do intervalo (padrão: 0).
- `stop`: Fim do intervalo (não incluído).
- `step`: (opcional) Incremento (padrão: 1).

Exemplos:
```python
for i in range(1, 10, 2):  # 1, 3, 5, 7, 9
    print(i)

for i in range(10, 0, -1):  # 10, 9, ..., 1
    print(i)
```

---

## **Iterando por Dicionários**

Ao usar um dicionário com `for`, você itera pelas **chaves** por padrão:

```python
aluno = {'nome': 'João', 'idade': 20, 'curso': 'Matemática'}

# Iterar sobre chaves
for chave in aluno:
    print(chave)

# Iterar sobre valores
for valor in aluno.values():
    print(valor)

# Iterar sobre itens (chave, valor)
for chave, valor in aluno.items():
    print(f'{chave}: {valor}')
```

---

## **Controlando o Fluxo**

### **`break`**
Interrompe o laço antes de terminar todas as iterações.
```python
for num in range(10):
    if num == 5:
        break
    print(num)  # 0, 1, 2, 3, 4
```

### **`continue`**
Pula para a próxima iteração do laço.
```python
for num in range(5):
    if num == 2:
        continue
    print(num)  # 0, 1, 3, 4
```

### **`else` com `for`**
A cláusula `else` é executada quando o laço termina sem interrupção (`break`).
```python
for num in range(5):
    print(num)
else:
    print("Fim do laço sem interrupções!")
```

---

## **Iterando com Funções Úteis**

### **`enumerate()`**
Adiciona um índice ao iterar por uma sequência.
```python
animais = ['gato', 'cachorro', 'coelho']
for indice, animal in enumerate(animais):
    print(f'{indice}: {animal}')
```

### **`zip()`**
Permite iterar sobre duas (ou mais) sequências ao mesmo tempo.
```python
nomes = ['Ana', 'Bruno', 'Carlos']
idades = [25, 30, 35]

for nome, idade in zip(nomes, idades):
    print(f'{nome} tem {idade} anos.')
```

---

## **Iterando com Conjuntos e Geradores**

### **Conjuntos**
A ordem dos elementos não é garantida.
```python
conjunto = {3, 1, 4, 1, 5}
for elemento in conjunto:
    print(elemento)
```

### **Geradores**
Iteração baseada em objetos que geram valores sob demanda.
```python
def gerador():
    for i in range(3):
        yield i

for valor in gerador():
    print(valor)
```

---

## **Exemplo Complexo**
Um laço que combina várias técnicas:
```python
produtos = ['Arroz', 'Feijão', 'Macarrão']
preços = [5.99, 4.99, 3.49]

for i, (produto, preço) in enumerate(zip(produtos, preços), start=1):
    print(f'{i}. {produto}: R${preço:.2f}')
```

Esse código exibe:
```
1. Arroz: R$5.99
2. Feijão: R$4.99
3. Macarrão: R$3.49
```

---
