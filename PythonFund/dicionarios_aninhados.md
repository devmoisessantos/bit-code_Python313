Com base no dicionário fornecido, podemos usar diferentes abordagens para analisá-lo e extrair informações úteis. Aqui estão exemplos práticos:

---

### **1. Visualização do Dicionário**
Para exibir o dicionário de forma mais clara:

#### **Usando `pprint`**
```python
import pprint

pprint.pprint(dicionario)
```

#### **Usando JSON**
```python
import json

print(json.dumps(dicionario, indent=4, ensure_ascii=False))
```

---

### **2. Percorrer o Dicionário**
Uma função recursiva pode ser útil para iterar sobre todas as chaves e valores.

```python
def percorrer_dicionario(d, nivel=0):
    for chave, valor in d.items():
        if isinstance(valor, dict):  # Se for um dicionário, entra nele
            print("  " * nivel + f"{chave}:")
            percorrer_dicionario(valor, nivel + 1)
        else:
            print("  " * nivel + f"{chave}: {valor}")

# Executando
percorrer_dicionario(dicionario)
```

Saída (exemplo):
```
_aninhado:
  nome: Moises
  idade: 26
endereco:
  rua: Av. Brasil
  numero: 123
  bairro: Centro
  cidade: Goiania
  estado: Goias
  pais: Brasil
telefone:
  principal: 123456789
  celular: 987654321
email:
  principal: k2H5K@example.com
  secundario: HgY3o@example.com
aniversario:
  dia: 15
  mes: 8
  ano: 2000
```

---

### **3. Acessar Dados Específicos**
Para acessar informações específicas diretamente:

```python
# Nome
print(dicionario['_aninhado']['nome'])

# Cidade
print(dicionario['endereco']['cidade'])

# Email principal
print(dicionario['email']['principal'])

# Aniversário formatado
aniversario = dicionario['aniversario']
print(f"{aniversario['dia']:02d}/{aniversario['mes']:02d}/{aniversario['ano']}")
```

---

### **4. Transformar em Dicionário Plano**
Para simplificar a análise, podemos achatar (flatten) o dicionário:

```python
def flatten_dict(d, prefix=""):
    items = {}
    for k, v in d.items():
        if isinstance(v, dict):
            items.update(flatten_dict(v, prefix + k + "."))
        else:
            items[prefix + k] = v
    return items

dicionario_plano = flatten_dict(dicionario)
pprint.pprint(dicionario_plano)
```

Saída:
```plaintext
{'_aninhado.idade': 26,
 '_aninhado.nome': 'Moises',
 'aniversario.ano': 2000,
 'aniversario.dia': 15,
 'aniversario.mes': 8,
 'email.principal': 'k2H5K@example.com',
 'email.secundario': 'HgY3o@example.com',
 'endereco.bairro': 'Centro',
 'endereco.cidade': 'Goiania',
 'endereco.estado': 'Goias',
 'endereco.numero': 123,
 'endereco.pais': 'Brasil',
 'endereco.rua': 'Av. Brasil',
 'telefone.celular': '987654321',
 'telefone.principal': '123456789'}
```

---

### **5. Transformar em DataFrame**
Se o dicionário contém dados tabulares (listas ou categorias), use o `pandas`:

```python
import pandas as pd

# Transformando a seção "endereco" em um DataFrame
endereco_df = pd.DataFrame([dicionario['endereco']])
print(endereco_df)

# Emails como DataFrame
email_df = pd.DataFrame([dicionario['email']])
print(email_df)
```

Saída:
**Endereço:**
```
            rua  numero  bairro    cidade estado   pais
0  Av. Brasil     123  Centro  Goiania  Goias  Brasil
```

**Emails:**
```
         principal         secundario
0  k2H5K@example.com  HgY3o@example.com
```

---

### **6. Buscar por uma Chave Específica**
Uma função genérica para encontrar uma chave em qualquer nível do dicionário:

```python
def buscar_chave(d, chave_procurada):
    if chave_procurada in d:
        return d[chave_procurada]
    for chave, valor in d.items():
        if isinstance(valor, dict):
            resultado = buscar_chave(valor, chave_procurada)
            if resultado is not None:
                return resultado
    return None

# Exemplo
print(buscar_chave(dicionario, 'cidade'))  # Saída: Goiania
print(buscar_chave(dicionario, 'principal'))  # Saída: 123456789
```

---
