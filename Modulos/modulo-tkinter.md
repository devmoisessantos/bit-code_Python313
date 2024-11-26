**tkinter**, o módulo padrão de Python para criação de interfaces gráficas (GUI):

---

## **Documentação Oficial do Tkinter**

O **Tkinter** é a biblioteca padrão para criar interfaces gráficas em Python, baseada no toolkit Tcl/Tk. A documentação completa para o Tkinter pode ser encontrada no site oficial do Python:

- [Documentação do Tkinter](https://docs.python.org/3/library/tkinter.html)

---

## **Principais Componentes do Tkinter**

### **Widgets Básicos**
- **`Button`**: Cria botões.
- **`Canvas`**: Usado para desenhar formas, gráficos e imagens.
- **`Checkbutton`**: Botões de seleção múltipla.
- **`Entry`**: Caixa de entrada de texto de uma única linha.
- **`Frame`**: Contêiner para organizar widgets.
- **`Label`**: Exibe texto ou imagens.
- **`Listbox`**: Lista de itens.
- **`Menu`**: Barra de menus ou menus suspensos.
- **`Message`**: Exibe texto multi-linha.
- **`Radiobutton`**: Botões de opção única.
- **`Scale`**: Controle deslizante.
- **`Scrollbar`**: Barra de rolagem.
- **`Text`**: Caixa de entrada de texto multi-linha.
- **`Toplevel`**: Janela separada da janela principal.

### **Gerenciamento de Layout**
- **`pack()`**: Organiza os widgets por empacotamento (direções específicas: cima, baixo, esquerda ou direita).
- **`grid()`**: Organiza widgets em uma grade (linhas e colunas).
- **`place()`**: Organiza widgets em posições absolutas.

### **Eventos e Bindings**
- Captura eventos do usuário, como cliques ou teclas pressionadas.
- Métodos principais:
  - **`bind()`**: Associa eventos a uma função.
  - **`unbind()`**: Remove associações.

### **Janelas e Diálogos**
- Criação de janelas modais ou caixas de diálogo padrão:
  - **`tkinter.filedialog`**: Caixas de diálogo para abrir e salvar arquivos.
  - **`tkinter.messagebox`**: Caixas de mensagens (informação, aviso, erro, etc.).

---

## **Exemplo Básico de Aplicação Tkinter**

```python
import tkinter as tk

# Criação da janela principal
root = tk.Tk()
root.title("Exemplo de Tkinter")
root.geometry("300x200")

# Adicionando um botão
button = tk.Button(root, text="Clique Aqui", command=lambda: print("Botão clicado!"))
button.pack(pady=20)

# Adicionando um rótulo
label = tk.Label(root, text="Olá, Mundo!", font=("Arial", 14))
label.pack()

# Loop principal da aplicação
root.mainloop()
```

---

## **Fontes Complementares**
1. **Tutoriais e exemplos práticos**:
   - [Python Tkinter Tutorial no Real Python](https://realpython.com/python-gui-tkinter/)
   - [Guia de Tkinter - TutorialsPoint](https://www.tutorialspoint.com/python/python_gui_programming.htm)

2. **Referência do Tcl/Tk**: A base do tkinter é o Tcl/Tk:
   - [Documentação Tcl/Tk](https://www.tcl.tk/doc/)
