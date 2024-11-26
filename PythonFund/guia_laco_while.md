Em Python, a estrutura de repetição `while` é usada para executar um bloco de código repetidamente enquanto uma condição for avaliada como verdadeira (`True`). Essa estrutura é útil quando não sabemos, a princípio, o número exato de iterações, mas temos uma condição lógica para controlar o fluxo.

Abaixo está uma explicação completa e exemplos práticos:

---

### **Sintaxe do `while`**
```python
while condição:
    # bloco de código a ser executado
```

- **`condição`**: Uma expressão booleana que será avaliada antes de cada iteração. Se for verdadeira, o bloco de código dentro do `while` será executado.
- O loop continuará até que a condição se torne falsa.

---

### **Comandos úteis com `while`**
1. **`break`**: Encerra o loop imediatamente, ignorando a condição.
2. **`continue`**: Pula para a próxima iteração, ignorando o código restante no bloco atual.
3. **`else`**: Opcionalmente, pode ser usado após o `while`. O bloco `else` será executado se o loop terminar normalmente (não interrompido por um `break`).

---

### **Exemplo básico**
```python
contador = 0

while contador < 5:
    print(f"Contador é {contador}")
    contador += 1  # Incrementa o contador

print("Loop finalizado.")
```

**Saída**:
```
Contador é 0
Contador é 1
Contador é 2
Contador é 3
Contador é 4
Loop finalizado.
```

---

### **Uso de `break`**
```python
while True:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        print("Encerrando...")
        break
    print(f"Você digitou: {numero}")
```

**Saída (interativa)**:
```
Digite um número (0 para sair): 3
Você digitou: 3
Digite um número (0 para sair): 5
Você digitou: 5
Digite um número (0 para sair): 0
Encerrando...
```

---

### **Uso de `continue`**
```python
contador = 0

while contador < 10:
    contador += 1
    if contador % 2 == 0:
        continue  # Pula números pares
    print(f"Número ímpar: {contador}")
```

**Saída**:
```
Número ímpar: 1
Número ímpar: 3
Número ímpar: 5
Número ímpar: 7
Número ímpar: 9
```

---

### **Uso de `else`**
```python
contador = 0

while contador < 3:
    print(f"Contador: {contador}")
    contador += 1
else:
    print("Loop terminou normalmente.")
```

**Saída**:
```
Contador: 0
Contador: 1
Contador: 2
Loop terminou normalmente.
```

---

### **Loop infinito**
Tenha cuidado com loops infinitos, pois podem travar seu programa:
```python
while True:
    print("Este é um loop infinito!")
    break  # Sempre use uma condição para sair
```

---

### **Exemplo prático: Jogo de adivinhação**
```python
import random

numero_secreto = random.randint(1, 10)
tentativas = 0

while True:
    chute = int(input("Adivinhe o número entre 1 e 10: "))
    tentativas += 1
    if chute == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break
    elif chute < numero_secreto:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")
```
