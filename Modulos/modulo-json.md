Guia completo sobre o módulo `json` no Python, com explicações sobre as funções mais utilizadas e exemplos. O módulo `json` é usado para trabalhar com dados no formato JSON (JavaScript Object Notation), que é amplamente usado para troca de informações em aplicações web.

---

### **Importação**
```python
import json
```

---

### **Funções principais**

#### **1. `json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, ... )`**
Escreve um objeto Python como uma representação JSON em um arquivo.

**Parâmetros:**
- `obj`: O objeto Python a ser serializado.
- `fp`: Arquivo ou objeto semelhante a arquivo para escrever o JSON.
- `skipkeys`: Ignora chaves que não são strings.
- `ensure_ascii`: Garante que o resultado seja ASCII.

**Exemplo:**
```python
data = {"name": "Moisés", "age": 25}
with open('data.json', 'w') as f:
    json.dump(data, f)
```

---

#### **2. `json.dumps(obj, *, skipkeys=False, ensure_ascii=True, ... )`**
Converte um objeto Python em uma string JSON.

**Parâmetros:** 
Igual ao `dump`, mas retorna uma string em vez de escrever em um arquivo.

**Exemplo:**
```python
data = {"name": "Moisés", "age": 25}
json_string = json.dumps(data, indent=4)
print(json_string)
```

---

#### **3. `json.load(fp, *, ... )`**
Lê um arquivo JSON e o converte para um objeto Python.

**Exemplo:**
```python
with open('data.json', 'r') as f:
    data = json.load(f)
print(data)
```

---

#### **4. `json.loads(s, *, ... )`**
Converte uma string JSON em um objeto Python.

**Exemplo:**
```python
json_string = '{"name": "Moisés", "age": 25}'
data = json.loads(json_string)
print(data)
```

---

### **Parâmetros adicionais importantes**
- **`indent`**: Formata o JSON para leitura humana.
  ```python
  json.dumps(data, indent=4)
  ```
- **`sort_keys`**: Ordena as chaves no JSON.
  ```python
  json.dumps(data, sort_keys=True)
  ```

---

### **Erros Comuns**
1. **`JSONDecodeError`**: Ocorre quando a string ou arquivo não é JSON válido.
   ```python
   invalid_json = '{"name": "Moisés", "age": }'
   data = json.loads(invalid_json)  # Levanta erro
   ```

2. **`TypeError`**: Tenta serializar objetos que não são JSON-serializáveis.
   ```python
   import datetime
   json.dumps(datetime.datetime.now())  # Levanta erro
   ```

---

### **Dicas avançadas**

#### **Serializar objetos personalizados**
Você pode usar o parâmetro `default` para lidar com objetos não serializáveis:
```python
import datetime

def custom_serializer(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    raise TypeError("Tipo não serializável")

data = {"time": datetime.datetime.now()}
json_string = json.dumps(data, default=custom_serializer)
print(json_string)
```

#### **Deserializar objetos personalizados**
Use o parâmetro `object_hook` para transformar dicionários JSON em objetos Python personalizados.
```python
def custom_deserializer(dct):
    if 'time' in dct:
        dct['time'] = datetime.datetime.fromisoformat(dct['time'])
    return dct

json_string = '{"time": "2024-11-25T10:00:00"}'
data = json.loads(json_string, object_hook=custom_deserializer)
print(data)
```

---

Para mais detalhes, consulte a [documentação oficial do Python sobre `json`](https://docs.python.org/3/library/json.html). 
