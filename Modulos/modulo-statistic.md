O módulo `statistics` em Python é usado para cálculos estatísticos básicos, como médias, variância, mediana e muito mais. Ele é parte da biblioteca padrão do Python, portanto, não precisa ser instalado separadamente.


---

## **1. Funções de Estatísticas de Localização**

### **`statistics.mean(data)`**
Calcula a média aritmética de um conjunto de dados.

- **Parâmetros**:  
  `data`: Sequência ou iterável de números.
- **Retorna**:  
  Média dos valores.

### **`statistics.median(data)`**
Calcula a mediana (valor central) de um conjunto de dados ordenados.

- **Parâmetros**:  
  `data`: Sequência ou iterável de números.
- **Retorna**:  
  Mediana dos valores.

### **`statistics.median_low(data)`**
Retorna a mediana baixa de um conjunto de dados ordenados.

- **Parâmetros**:  
  Igual ao `median`.
- **Retorna**:  
  Valor menor no caso de duas medianas possíveis.

### **`statistics.median_high(data)`**
Retorna a mediana alta de um conjunto de dados ordenados.

- **Parâmetros**:  
  Igual ao `median`.
- **Retorna**:  
  Valor maior no caso de duas medianas possíveis.

### **`statistics.mode(data)`**
Retorna o valor mais comum (moda) em um conjunto de dados.

- **Parâmetros**:  
  `data`: Sequência ou iterável de números ou strings.
- **Retorna**:  
  Valor mais frequente.  
- **Erro**:  
  Levanta `StatisticsError` se não houver uma moda única.

### **`statistics.fmean(data)`**  
Calcula a média aritmética, retornando um número de ponto flutuante.

- **Parâmetros**:  
  `data`: Sequência ou iterável de números.
- **Retorna**:  
  Média como ponto flutuante.

---

## **2. Funções de Estatísticas de Dispersão**

### **`statistics.pvariance(data, mu=None)`**
Calcula a variância populacional.

- **Parâmetros**:  
  - `data`: Sequência ou iterável de números.
  - `mu`: Opcional, a média populacional.
- **Retorna**:  
  Variância dos valores.

### **`statistics.variance(data, xbar=None)`**
Calcula a variância amostral.

- **Parâmetros**:  
  - `data`: Sequência ou iterável de números.
  - `xbar`: Opcional, a média da amostra.
- **Retorna**:  
  Variância dos valores.

### **`statistics.stdev(data, xbar=None)`**
Calcula o desvio padrão amostral.

- **Parâmetros**:  
  - `data`: Sequência ou iterável de números.
  - `xbar`: Opcional, a média da amostra.
- **Retorna**:  
  Desvio padrão.

### **`statistics.pstdev(data, mu=None)`**
Calcula o desvio padrão populacional.

- **Parâmetros**:  
  - `data`: Sequência ou iterável de números.
  - `mu`: Opcional, a média populacional.
- **Retorna**:  
  Desvio padrão.

---

## **3. Funções de Estatísticas Robustas**

### **`statistics.harmonic_mean(data)`**
Calcula a média harmônica de um conjunto de dados.

- **Parâmetros**:  
  `data`: Sequência ou iterável de números positivos.
- **Retorna**:  
  Média harmônica.

### **`statistics.geometric_mean(data)`**
Calcula a média geométrica de um conjunto de dados.

- **Parâmetros**:  
  `data`: Sequência ou iterável de números não negativos.
- **Retorna**:  
  Média geométrica.

---

## **4. Funções para Trabalhar com Multimodalidade**

### **`statistics.multimode(data)`**
Retorna uma lista de todos os valores mais frequentes (modas) em um conjunto de dados.

- **Parâmetros**:  
  `data`: Sequência ou iterável.
- **Retorna**:  
  Lista de modas.

---

## **5. Outros Recursos e Observações**

- **Erros Levantados**:  
  - `StatisticsError`: Usado quando os dados fornecidos são insuficientes ou inválidos para cálculos (por exemplo, lista vazia para `mean()`).
- **Suporte a Tipos Numéricos**:  
  Funciona com tipos como `int`, `float`, e `Decimal`.

---

### **Exemplo Prático**

```python
import statistics

data = [1, 2, 3, 4, 5, 6, 6]

# Média
print("Média:", statistics.mean(data))

# Mediana
print("Mediana:", statistics.median(data))

# Moda
print("Moda:", statistics.mode(data))

# Variância
print("Variância:", statistics.variance(data))

# Desvio padrão
print("Desvio padrão:", statistics.stdev(data))
```

Para mais informações, confira a [documentação oficial do Python](https://docs.python.org/3/library/statistics.html).