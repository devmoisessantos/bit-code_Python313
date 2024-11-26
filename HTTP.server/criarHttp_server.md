
1. Descobre automaticamente o IP da máquina.
2. Inicia o servidor HTTP na porta desejada.
3. Exibe o endereço para acesso no celular.

Você pode usar esse script tanto no PC quanto no Termux.

---

### **Código para Automação**
Crie um arquivo Python (por exemplo, `share_files.py`) com o seguinte conteúdo:

```python
import os
import socket
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

def get_local_ip():
    """Obtém o IP local da máquina."""
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

def start_http_server(port=8080):
    """Inicia o servidor HTTP na porta especificada."""
    # Obtém o IP local
    ip_address = get_local_ip()
    
    # Exibe as instruções para o usuário
    print(f"\n📂 Servidor iniciado!")
    print(f"🌐 Acesse no navegador do celular:")
    print(f"    http://{ip_address}:{port}")
    print("\n🛑 Pressione Ctrl+C para encerrar o servidor.")

    # Inicia o servidor HTTP
    with TCPServer(("", port), SimpleHTTPRequestHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🔴 Servidor encerrado!")

if __name__ == "__main__":
    # Define o diretório a ser compartilhado
    shared_folder = input("Digite o caminho da pasta a ser compartilhada (ou pressione Enter para usar a pasta atual): ").strip()
    if shared_folder:
        os.chdir(shared_folder)
    else:
        print("Compartilhando a pasta atual.\n")

    # Define a porta
    port = 8080
    start_http_server(port)
```

---

### **Como usar**

#### No PC:
1. Salve o script (`share_files.py`) em um diretório acessível.
2. Execute no terminal:
   ```bash
   python share_files.py
   ```
3. Insira o caminho da pasta que deseja compartilhar ou pressione **Enter** para usar a pasta atual.
4. Acesse o endereço exibido no celular (exemplo: `http://192.168.1.100:8080`).

#### No Termux:
1. Copie o arquivo para o Termux ou crie diretamente nele.
2. Execute o script:
   ```bash
   python share_files.py
   ```
3. Insira o caminho da pasta ou pressione Enter.
4. Conecte o celular à mesma rede Wi-Fi e acesse o endereço exibido.

---

### **Opcional: Tornar o Script Executável**
#### Windows:
1. Crie um arquivo `.bat` para rodar o script:
   ```bat
   @echo off
   python path\to\share_files.py
   pause
   ```

#### Termux/Linux:
1. Torne o script executável:
   ```bash
   chmod +x share_files.py
   ```
2. Execute diretamente:
   ```bash
   ./share_files.py
   ```
