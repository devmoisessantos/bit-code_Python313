
---

## 1. Criar o Ambiente Virtual
1. Navegue até o diretório `Desktop`:
   ```bash
   cd C:\Users\meu-p\Desktop
   ```

2. Crie o diretório `Modulos` (se ainda não existir):
   ```bash
   mkdir Modulos
   ```

3. Entre na pasta `Modulos`:
   ```bash
   cd Modulos
   ```

4. Crie o ambiente virtual chamado `.venv`:
   ```bash
   python3 -m venv .venv
   ```

Após esse comando, uma pasta chamada `.venv` será criada dentro de `Modulos`, contendo os arquivos necessários para o ambiente virtual.

---

## 2. Ativar o Ambiente Virtual
Estando no diretório `C:\Users\meu-p\Desktop\Modulos`, ative o ambiente virtual com o comando:

### No Windows:
```bash
.venv\Scripts\activate
```

Se o ambiente foi ativado com sucesso, o prompt do terminal mostrará o prefixo `(.venv)`:
```bash
(.venv) PS C:\Users\meu-p\Desktop\Modulos>
```

---

## 3. Desativar o Ambiente Virtual
Para desativar o ambiente virtual, digite:
```bash
deactivate
```

O prefixo `(.venv)` desaparecerá, indicando que o ambiente virtual foi desativado:
```bash
PS C:\Users\meu-p\Desktop\Modulos>
```

---

### Resumo dos Comandos Utilizados:
1. Criar a pasta e o ambiente virtual:
   ```bash
   cd C:\Users\meu-p\Desktop
   mkdir Modulos
   cd Modulos
   python3 -m venv .venv
   ```

2. Ativar o ambiente virtual:
   ```bash
   .venv\Scripts\activate
   ```

3. Desativar o ambiente virtual:
   ```bash
   deactivate
   ```
