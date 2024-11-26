O módulo `os` do Python fornece uma maneira de interagir com o sistema operacional. Ele inclui funções para manipulação de arquivos, diretórios, processos e informações do sistema operacional. 

---

### **Importação do módulo**
```python
import os
```

---

### **Gerenciamento de Arquivos e Diretórios**

#### Obter o diretório de trabalho atual:
```python
os.getcwd()
```

#### Alterar o diretório de trabalho:
```python
os.chdir('caminho/para/diretorio')
```

#### Criar um diretório:
```python
os.mkdir('nome_diretorio')
```

#### Criar diretórios aninhados:
```python
os.makedirs('caminho/diretorios/aninhados')
```

#### Remover um diretório vazio:
```python
os.rmdir('nome_diretorio')
```

#### Remover diretórios aninhados:
```python
os.removedirs('caminho/diretorios/aninhados')
```

#### Listar arquivos e diretórios:
```python
os.listdir('caminho')  # Retorna uma lista com nomes de arquivos/diretórios
```

#### Verificar existência de arquivo/diretório:
```python
os.path.exists('caminho/arquivo_ou_diretorio')
```

#### Renomear arquivo ou diretório:
```python
os.rename('nome_atual', 'novo_nome')
```

#### Excluir arquivo:
```python
os.remove('nome_arquivo')
```

---

### **Informações de Arquivo**

#### Obter tamanho de um arquivo:
```python
os.path.getsize('caminho/arquivo')
```

#### Obter caminho absoluto:
```python
os.path.abspath('caminho/relativo')
```

#### Obter nome do diretório de um caminho:
```python
os.path.dirname('caminho/arquivo')
```

#### Obter nome do arquivo de um caminho:
```python
os.path.basename('caminho/arquivo')
```

#### Dividir caminho em diretório e arquivo:
```python
os.path.split('caminho/arquivo')
```

#### Unir caminhos:
```python
os.path.join('caminho1', 'caminho2')
```

#### Verificar se é um arquivo:
```python
os.path.isfile('caminho/arquivo')
```

#### Verificar se é um diretório:
```python
os.path.isdir('caminho/diretorio')
```

---

### **Interação com o Sistema Operacional**

#### Executar comandos no terminal:
```python
os.system('comando_terminal')
```

#### Obter variáveis de ambiente:
```python
os.environ  # Retorna um dicionário com as variáveis
os.getenv('NOME_VARIAVEL')  # Retorna o valor de uma variável específica
```

#### Definir uma variável de ambiente:
```python
os.environ['NOME_VARIAVEL'] = 'valor'
```

#### Identificar o sistema operacional:
```python
os.name  # Retorna 'posix', 'nt', 'os2', etc.
```

---

### **Manipulação de Processos**

#### Obter ID do processo atual:
```python
os.getpid()
```

#### Obter ID do usuário:
```python
os.getuid()  # Apenas em sistemas Unix
```

#### Obter ID do grupo:
```python
os.getgid()  # Apenas em sistemas Unix
```

#### Criar processos filhos:
```python
pid = os.fork()  # Apenas em sistemas Unix
```

#### Esperar o término de um processo filho:
```python
os.wait()
```

---

### **Permissões e Propriedades**

#### Alterar permissões de arquivo:
```python
os.chmod('caminho/arquivo', modo)
```

#### Alterar proprietário de arquivo:
```python
os.chown('caminho/arquivo', uid, gid)  # Apenas em sistemas Unix
```

#### Alterar timestamp de um arquivo:
```python
os.utime('caminho/arquivo', (tempo_acesso, tempo_modificacao))
```

---

### **Outras Funcionalidades Úteis**

#### Caminho da raiz do sistema:
```python
os.path.sep  # Retorna o separador de diretórios ('/' ou '\')
```

#### Determinar se o sistema usa simbolismo de links:
```python
os.path.islink('caminho')
```

#### Criar um link simbólico:
```python
os.symlink('arquivo_alvo', 'link_nome')
```

#### Acessar informações detalhadas de um arquivo:
```python
os.stat('caminho/arquivo')
```

---

### **Exemplo Completo**
Aqui está um exemplo prático que combina várias funções do módulo `os`:

```python
import os

# Diretório atual
print("Diretório atual:", os.getcwd())

# Listar arquivos no diretório
arquivos = os.listdir('.')
print("Arquivos no diretório:", arquivos)

# Criar novo diretório
os.mkdir('novo_diretorio')

# Verificar existência de diretório
if os.path.exists('novo_diretorio'):
    print("Diretório criado com sucesso!")

# Renomear diretório
os.rename('novo_diretorio', 'diretorio_renomeado')

# Remover diretório
os.rmdir('diretorio_renomeado')
print("Diretório removido com sucesso!")
```

---
