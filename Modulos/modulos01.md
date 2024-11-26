## **10. Criando módulos reutilizáveis para projetos maiores**

Ao projetar sistemas maiores, os módulos precisam ser estruturados para maximizar a **reutilização** e **manutenção**. Aqui estão estratégias para criar módulos eficientes:

---

### **10.1 Módulos com variáveis globais configuráveis**

Uma prática comum é criar um módulo separado para **configurações globais**, que pode ser acessado por outras partes do sistema.

#### **Exemplo: Configurações globais (`config.py`)**
```python
# config.py
APP_NAME = "Minha Aplicação"
VERSAO = "1.0.0"
DEBUG = True
```

#### **Usando o módulo `config`**
```python
# main.py
import config

print(f"{config.APP_NAME} - Versão {config.VERSAO}")
if config.DEBUG:
    print("Modo de depuração ativado!")
```

---

### **10.2 Organizando funções utilitárias**

Concentre funções usadas em várias partes do sistema em um módulo utilitário.

#### **Exemplo: Módulo utilitário (`utils.py`)**
```python
# utils.py
def formata_moeda(valor):
    """Formata um valor numérico em formato monetário."""
    return f"R$ {valor:,.2f}".replace(",", ".")

def ler_arquivo(caminho):
    """Lê o conteúdo de um arquivo de texto."""
    with open(caminho, 'r') as arquivo:
        return arquivo.read()
```

#### **Uso prático**
```python
# main.py
from utils import formata_moeda, ler_arquivo

print(formata_moeda(12345.67))  # Saída: R$ 12.345,67
conteudo = ler_arquivo("exemplo.txt")
print("Conteúdo do arquivo:", conteudo)
```

---

### **10.3 Criação de módulos interdependentes**

Módulos podem interagir entre si dentro de um pacote, mas evite **dependências circulares** (módulo A importa módulo B, que importa módulo A).

#### **Estrutura:**
```
meu_projeto/
    __init__.py
    calculadora.py
    relatorios.py
```

#### **Exemplo: `calculadora.py`**
```python
# calculadora.py
def soma(a, b):
    return a + b
```

#### **Exemplo: `relatorios.py`**
```python
# relatorios.py
from calculadora import soma

def gerar_relatorio():
    total = soma(100, 200)
    print(f"Relatório gerado: Total calculado = {total}")
```

#### **Uso:**
```python
from relatorios import gerar_relatorio

gerar_relatorio()
```

---

## **11. Lidando com grandes pacotes e dependências**

Em projetos de larga escala, é comum ter dependências complexas. Use ferramentas como `requirements.txt` e **virtual environments** para manter a organização.

---

### **11.1 Gerando um arquivo `requirements.txt`**

Liste todos os pacotes de terceiros usados no projeto:
```bash
pip freeze > requirements.txt
```

### **11.2 Instalando dependências a partir de `requirements.txt`**
```bash
pip install -r requirements.txt
```

---

## **12. Ferramentas adicionais para documentação e qualidade de código**

### **12.1 Incluindo docstrings detalhadas**

Sempre documente suas funções, módulos e classes com docstrings.

#### **Exemplo:**
```python
def calcula_media(valores):
    """
    Calcula a média de uma lista de números.

    Args:
        valores (list): Uma lista de números inteiros ou float.

    Returns:
        float: A média dos números na lista.
    """
    return sum(valores) / len(valores)
```

### **12.2 Gerando documentação automaticamente**

Use ferramentas como [Sphinx](https://www.sphinx-doc.org/) para criar uma documentação profissional a partir de docstrings.

---

## **13. Dicas finais para trabalhar com módulos e pacotes**

1. **Evite dependências circulares**: Estruture o código para evitar que dois módulos importem-se mutuamente.
2. **Use aliases**: Para manter o código limpo, use `as` ao importar módulos com nomes longos.
   ```python
   import pandas as pd
   ```
3. **Mantenha um estilo consistente**: Siga as diretrizes da [PEP 8](https://peps.python.org/pep-0008/) para nomes de módulos e funções.
4. **Teste seus módulos isoladamente**: Use frameworks como `unittest` ou `pytest` para garantir que cada módulo funcione como esperado.

---
