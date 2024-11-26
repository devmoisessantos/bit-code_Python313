
---

### Introdução
O módulo `math` fornece funções matemáticas definidas pela biblioteca C subjacente. Ele é utilizado para cálculos matemáticos mais avançados do que os operadores padrão.

### Importação
Para usar o módulo, você precisa importá-lo:  
```python
import math
```

---

### Constantes
1. **`math.pi`**  
   - O valor de π (pi): 3.141592653589793.
   - Exemplo:
     ```python
     print(math.pi)  # 3.141592653589793
     ```

2. **`math.e`**  
   - A base do logaritmo natural (e): 2.718281828459045.

3. **`math.tau`**  
   - O valor de τ (tau): 6.283185307179586.  
     (τ = 2π)

4. **`math.inf`**  
   - Representa infinito (∞).  
     Exemplo:
     ```python
     print(math.inf > 1000)  # True
     ```

5. **`math.nan`**  
   - Representa "Not a Number" (NaN).  
     Usado para valores indefinidos ou não representáveis.

---

### Funções Matemáticas Gerais
1. **`math.ceil(x)`**  
   - Retorna o menor inteiro maior ou igual a `x`.
   - Exemplo:
     ```python
     print(math.ceil(4.2))  # 5
     ```

2. **`math.floor(x)`**  
   - Retorna o maior inteiro menor ou igual a `x`.
   - Exemplo:
     ```python
     print(math.floor(4.8))  # 4
     ```

3. **`math.fabs(x)`**  
   - Retorna o valor absoluto de `x` como ponto flutuante.
   - Exemplo:
     ```python
     print(math.fabs(-5.3))  # 5.3
     ```

4. **`math.factorial(x)`**  
   - Retorna o fatorial de `x` (inteiro não negativo).
   - Exemplo:
     ```python
     print(math.factorial(5))  # 120
     ```

5. **`math.isfinite(x)`**  
   - Retorna `True` se `x` for finito.
   - Exemplo:
     ```python
     print(math.isfinite(100))  # True
     print(math.isfinite(math.inf))  # False
     ```

6. **`math.isinf(x)`**  
   - Retorna `True` se `x` for infinito.

7. **`math.isnan(x)`**  
   - Retorna `True` se `x` for NaN.

8. **`math.trunc(x)`**  
   - Trunca `x` para um inteiro (elimina a parte decimal).
   - Exemplo:
     ```python
     print(math.trunc(5.8))  # 5
     ```

---

### Funções Exponenciais e Logarítmicas
1. **`math.exp(x)`**  
   - Retorna `e**x`.

2. **`math.log(x, base)`**  
   - Calcula o logaritmo de `x` na base especificada.  
     Se `base` não for informada, calcula o logaritmo natural (base `e`).

3. **`math.log2(x)`**  
   - Calcula o logaritmo base 2 de `x`.

4. **`math.log10(x)`**  
   - Calcula o logaritmo base 10 de `x`.

5. **`math.pow(x, y)`**  
   - Retorna `x` elevado à potência `y`.

6. **`math.sqrt(x)`**  
   - Retorna a raiz quadrada de `x`.

---

### Funções Trigonométricas
1. **`math.sin(x)`**  
   - Retorna o seno de `x` (em radianos).

2. **`math.cos(x)`**  
   - Retorna o cosseno de `x` (em radianos).

3. **`math.tan(x)`**  
   - Retorna a tangente de `x` (em radianos).

4. **`math.asin(x)`**  
   - Retorna o arco-seno de `x` (resultado em radianos).

5. **`math.acos(x)`**  
   - Retorna o arco-cosseno de `x`.

6. **`math.atan(x)`**  
   - Retorna o arco-tangente de `x`.

7. **`math.degrees(x)`**  
   - Converte radianos para graus.

8. **`math.radians(x)`**  
   - Converte graus para radianos.

---

### Funções Hiperbólicas
1. **`math.sinh(x)`**  
   - Retorna o seno hiperbólico de `x`.

2. **`math.cosh(x)`**  
   - Retorna o cosseno hiperbólico de `x`.

3. **`math.tanh(x)`**  
   - Retorna a tangente hiperbólica de `x`.

4. **`math.asinh(x)`**  
   - Retorna o arco-seno hiperbólico de `x`.

5. **`math.acosh(x)`**  
   - Retorna o arco-cosseno hiperbólico de `x`.

6. **`math.atanh(x)`**  
   - Retorna o arco-tangente hiperbólico de `x`.

---

### Funções de Arredondamento e Precisão
1. **`math.copysign(x, y)`**  
   - Retorna `x` com o sinal de `y`.
   - Exemplo:
     ```python
     print(math.copysign(5, -1))  # -5
     ```

2. **`math.fmod(x, y)`**  
   - Retorna o resto da divisão de `x` por `y`.

3. **`math.frexp(x)`**  
   - Retorna uma tupla `(m, e)` tal que `x = m * 2**e`.

4. **`math.ldexp(x, i)`**  
   - Calcula `x * (2**i)`.

5. **`math.modf(x)`**  
   - Retorna a parte fracionária e a parte inteira de `x` como uma tupla.

6. **`math.isclose(a, b, rel_tol, abs_tol)`**  
   - Verifica se dois valores estão próximos, considerando tolerâncias relativas e absolutas.

---
