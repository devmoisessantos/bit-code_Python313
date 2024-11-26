
---

## **Documentação do Módulo `hashlib`**

O módulo `hashlib` fornece interfaces para algoritmos de hash criptográficos seguros, como SHA-1, SHA-256, MD5 e outros. É amplamente utilizado para verificar integridade de dados e armazenamento de senhas.

### **Importação do Módulo**

```python
import hashlib
```

---

### **Algoritmos Disponíveis**

Os algoritmos mais comuns incluem:
- **SHA-1**: `sha1()`
- **SHA-224**: `sha224()`
- **SHA-256**: `sha256()`
- **SHA-384**: `sha384()`
- **SHA-512**: `sha512()`
- **MD5**: `md5()` *(não recomendado para fins de segurança)*

Para verificar os algoritmos suportados no seu sistema:

```python
print(hashlib.algorithms_guaranteed)
# Retorna um conjunto dos algoritmos garantidos
print(hashlib.algorithms_available)
# Retorna todos os algoritmos disponíveis (inclui alguns específicos da plataforma)
```

---

### **Uso Básico**

1. **Criar um objeto de hash**
   Cada algoritmo de hash possui um construtor, como `hashlib.sha256()`.

   ```python
   hash_obj = hashlib.sha256()
   ```

2. **Adicionar dados ao hash**
   Use o método `.update(data)` para adicionar os dados. O argumento deve ser em bytes.

   ```python
   hash_obj.update(b'Hello World')
   ```

3. **Obter o valor do hash**
   - **Hexadecimal**: `hexdigest()` retorna o hash como uma string hexadecimal.
   - **Binário**: `digest()` retorna o hash em bytes.

   ```python
   print(hash_obj.hexdigest())  # Exemplo: 'a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32baf04a57a'
   print(hash_obj.digest())     # Bytes equivalentes
   ```

---

### **Exemplo Completo**

Aqui está um exemplo para calcular o SHA-256 de uma string:

```python
import hashlib

# Dados a serem hashados
data = "Mensagem secreta"
data_bytes = data.encode('utf-8')  # Converte a string para bytes

# Criar o hash SHA-256
hash_sha256 = hashlib.sha256()
hash_sha256.update(data_bytes)

# Obter o hash em hexadecimal
print("Hash SHA-256:", hash_sha256.hexdigest())
```

---

### **Hash Direto (Atalho)**

Você pode calcular o hash de uma mensagem diretamente sem criar um objeto separadamente:

```python
hash_sha256 = hashlib.sha256(b"Mensagem secreta").hexdigest()
print("Hash SHA-256:", hash_sha256)
```

---

### **Trabalhando com Arquivos**

Para calcular o hash de arquivos (por exemplo, SHA-1):

```python
import hashlib

def hash_file(filename, algorithm='sha256'):
    hash_obj = getattr(hashlib, algorithm)()
    with open(filename, 'rb') as f:
        while chunk := f.read(8192):  # Lê o arquivo em blocos de 8 KB
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

# Exemplo de uso
file_hash = hash_file("caminho/para/seu/arquivo.txt", algorithm='sha1')
print("Hash SHA-1 do arquivo:", file_hash)
```

---

### **HMAC (Hashes com Chave Secreta)**

O módulo `hashlib` também suporta HMAC (Hash-based Message Authentication Code):

```python
import hmac
import hashlib

key = b"chave_secreta"
message = b"mensagem_importante"

hmac_result = hmac.new(key, message, hashlib.sha256).hexdigest()
print("HMAC-SHA256:", hmac_result)
```

---

### **Customizando Algoritmos (via OpenSSL)**

Se o seu ambiente suporta OpenSSL, você pode acessar algoritmos adicionais:

```python
hash_obj = hashlib.new('blake2b')
hash_obj.update(b"mensagem")
print(hash_obj.hexdigest())
```

---

### **Notas para Usuários do Windows**

- Certifique-se de que sua versão do Python está atualizada (Python 3.6 ou superior é recomendado).
- Para algoritmos adicionais, verifique se OpenSSL está instalado no sistema.
- No Windows, você pode usar `py -m pip install` para instalar pacotes relacionados a hash se necessário.

---

Esses são os algoritmos de hash mais comuns disponíveis no módulo `hashlib`, com uma breve descrição de cada um:

### **1. Algoritmos SHA-2 e SHA-3**

SHA (Secure Hash Algorithm) é um conjunto de funções de hash criptográficas.

- **`sha224`**: Produz hashes de 224 bits. É parte do SHA-2.
- **`sha256`**: Produz hashes de 256 bits. Popular por sua segurança e uso em aplicações modernas.
- **`sha384`**: Produz hashes de 384 bits.
- **`sha512`**: Produz hashes de 512 bits. É o mais seguro no SHA-2.
  
SHA-3 é uma versão mais recente do SHA, baseada na função Keccak:
- **`sha3_224`**: Produz hashes de 224 bits, como o SHA-224, mas com um design diferente.
- **`sha3_256`**: Produz hashes de 256 bits, como o SHA-256.
- **`sha3_384`**: Produz hashes de 384 bits, como o SHA-384.
- **`sha3_512`**: Produz hashes de 512 bits, como o SHA-512.

---

### **2. MD5**

- **`md5`**: Produz hashes de 128 bits. É rápido, mas não é mais considerado seguro para uso em aplicações que requerem proteção contra colisões ou ataques. Use apenas em contextos onde a segurança não é essencial (como verificações simples de integridade de dados).

---

### **3. BLAKE2**

BLAKE2 é uma alternativa mais rápida e eficiente ao SHA-2 e SHA-3.

- **`blake2s`**: Produz hashes de 256 bits para sistemas leves.
- **`blake2b`**: Produz hashes de 512 bits, ideal para sistemas de alto desempenho.

---

### **4. SHAKE (Funções de Hash XOF)**

SHAKE (Secure Hash Algorithm with Extensible Output Function) é uma função de hash configurável, que permite especificar o comprimento do hash.

- **`shake_128`**: Extensible Output Function baseada em Keccak, segura até 128 bits de segurança.
- **`shake_256`**: Extensible Output Function baseada em Keccak, segura até 256 bits de segurança.

**Exemplo de uso do SHAKE** (note que você precisa especificar o tamanho do hash na saída):

```python
import hashlib

data = b"mensagem importante"

# SHAKE-128 com 32 bytes (256 bits)
shake = hashlib.shake_128(data)
print(shake.hexdigest(32))  # 32 bytes = 256 bits
```

---

### **5. SHA-1**

- **`sha1`**: Produz hashes de 160 bits. Não é mais considerado seguro para aplicações que precisam de forte resistência a colisões. Pode ser usado para verificações de integridade em sistemas legados.

---

### **Escolha do Algoritmo**

1. **Segurança moderna**: Prefira `sha256`, `sha3_256`, `blake2b` ou `blake2s`.
2. **Integridade simples**: `md5` ou `sha1` para contextos onde segurança não é crítica.
3. **Flexibilidade**: Use `shake_128` ou `shake_256` se precisar ajustar o tamanho do hash.

