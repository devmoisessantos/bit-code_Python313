O módulo `random` do Python fornece funções para gerar números aleatórios e realizar operações relacionadas à aleatoriedade.

---

## **Funções principais do módulo `random`**

### **1. Geração de números aleatórios básicos**
- `random.random()`: Retorna um número de ponto flutuante aleatório no intervalo `[0.0, 1.0)`.
- `random.uniform(a, b)`: Retorna um número de ponto flutuante aleatório no intervalo `[a, b]` ou `[b, a]`, dependendo de qual for maior.
- `random.randint(a, b)`: Retorna um número inteiro aleatório no intervalo `[a, b]` (inclusive).
- `random.randrange(start, stop[, step])`: Retorna um número inteiro aleatório dentro de um intervalo especificado (similar a `range()`).
- `random.choice(seq)`: Retorna um elemento aleatório de uma sequência (lista, tupla, string, etc.).

---

### **2. Operações com sequências**
- `random.shuffle(seq[, random])`: Embaralha os elementos de uma lista (modifica a lista original).
- `random.sample(population, k)`: Retorna uma nova lista contendo `k` elementos distintos selecionados aleatoriamente da população.

---

### **3. Geração de valores ponderados**
- `random.choices(population, weights=None, *, cum_weights=None, k=1)`: Retorna uma lista de `k` elementos aleatórios, podendo usar pesos para influenciar a probabilidade de cada elemento ser escolhido.

---

### **4. Geração de valores a partir de distribuições**
- `random.gauss(mu, sigma)`: Retorna um valor seguindo a distribuição normal (Gaussiana) com média `mu` e desvio padrão `sigma`.
- `random.expovariate(lambd)`: Retorna um valor seguindo a distribuição exponencial com taxa `lambd`.
- `random.gammavariate(alpha, beta)`: Retorna um valor seguindo a distribuição gama.
- `random.lognormvariate(mu, sigma)`: Retorna um valor seguindo a distribuição log-normal.
- `random.normalvariate(mu, sigma)`: Retorna um valor seguindo a distribuição normal.
- `random.vonmisesvariate(mu, kappa)`: Retorna um valor seguindo a distribuição de Von Mises.
- `random.paretovariate(alpha)`: Retorna um valor seguindo a distribuição de Pareto.
- `random.weibullvariate(alpha, beta)`: Retorna um valor seguindo a distribuição de Weibull.
  
---

### **5. Configuração do gerador de números aleatórios**
- `random.seed(a=None, version=2)`: Inicializa o gerador de números aleatórios. Pode usar um valor específico para tornar os resultados reproduzíveis.
- `random.getstate()`: Retorna o estado interno atual do gerador de números aleatórios.
- `random.setstate(state)`: Restaura o estado do gerador para um estado retornado por `getstate()`.

---

### **6. Uso de geradores personalizados**
O módulo também suporta geradores personalizados com a classe `random.Random`. Isso permite criar instâncias separadas de geradores de números aleatórios com seu próprio estado independente.

```python
from random import Random

rand_gen = Random()
rand_gen.seed(123)
print(rand_gen.random())  # Gera números de forma independente
```

---

### **Exemplo de uso prático**

```python
import random

# Número flutuante entre 0 e 1
print(random.random())

# Número inteiro entre 1 e 10
print(random.randint(1, 10))

# Embaralhar uma lista
lista = [1, 2, 3, 4, 5]
random.shuffle(lista)
print(lista)

# Escolher 2 elementos de uma lista com pesos
itens = ['maçã', 'banana', 'laranja']
pesos = [10, 1, 1]
print(random.choices(itens, weights=pesos, k=2))

# Número a partir de uma distribuição normal
print(random.normalvariate(mu=0, sigma=1))
```

Para mais informações, consulte a [documentação oficial do Python](https://docs.python.org/3/library/random.html).