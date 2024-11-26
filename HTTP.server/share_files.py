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
