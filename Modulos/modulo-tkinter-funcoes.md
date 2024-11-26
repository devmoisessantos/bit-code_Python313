Exemplos básicos para cada método ou recurso principal do **Tkinter** 

---

## **Widgets Básicos**

### **1. Button**
```python
import tkinter as tk

root = tk.Tk()
button = tk.Button(root, text="Clique Aqui", command=lambda: print("Botão clicado!"))
button.pack()
root.mainloop()
```

---

### **2. Canvas**
```python
import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=200, height=100, bg="lightblue")
canvas.pack()
canvas.create_rectangle(50, 20, 150, 80, fill="red")
root.mainloop()
```

---

### **3. Checkbutton**
```python
import tkinter as tk

root = tk.Tk()
var = tk.BooleanVar()

check = tk.Checkbutton(root, text="Aceito os termos", variable=var)
check.pack()

button = tk.Button(root, text="Confirmar", command=lambda: print("Aceito" if var.get() else "Não aceito"))
button.pack()

root.mainloop()
```

---

### **4. Entry**
```python
import tkinter as tk

root = tk.Tk()
entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Enviar", command=lambda: print("Texto digitado:", entry.get()))
button.pack()

root.mainloop()
```

---

### **5. Frame**
```python
import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root, bg="blue", width=200, height=100)
frame.pack(padx=10, pady=10)
root.mainloop()
```

---

### **6. Label**
```python
import tkinter as tk

root = tk.Tk()
label = tk.Label(root, text="Olá, Tkinter!", font=("Arial", 16), fg="blue")
label.pack()
root.mainloop()
```

---

### **7. Listbox**
```python
import tkinter as tk

root = tk.Tk()
listbox = tk.Listbox(root)
listbox.pack()
for item in ["Item 1", "Item 2", "Item 3"]:
    listbox.insert(tk.END, item)

button = tk.Button(root, text="Mostrar Seleção", command=lambda: print("Selecionado:", listbox.get(tk.ACTIVE)))
button.pack()

root.mainloop()
```

---

### **8. Menu**
```python
import tkinter as tk

def hello():
    print("Menu clicado!")

root = tk.Tk()
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Novo", command=hello)
filemenu.add_command(label="Abrir", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Sair", command=root.quit)
menubar.add_cascade(label="Arquivo", menu=filemenu)

root.config(menu=menubar)
root.mainloop()
```

---

### **9. Message**
```python
import tkinter as tk

root = tk.Tk()
message = tk.Message(root, text="Isso é uma mensagem multi-linha com Tkinter!", width=200)
message.pack()
root.mainloop()
```

---

### **10. Radiobutton**
```python
import tkinter as tk

root = tk.Tk()
var = tk.StringVar(value="Opção 1")

radio1 = tk.Radiobutton(root, text="Opção 1", variable=var, value="Opção 1")
radio1.pack()
radio2 = tk.Radiobutton(root, text="Opção 2", variable=var, value="Opção 2")
radio2.pack()

button = tk.Button(root, text="Confirmar", command=lambda: print("Selecionado:", var.get()))
button.pack()

root.mainloop()
```

---

### **11. Scale**
```python
import tkinter as tk

root = tk.Tk()
scale = tk.Scale(root, from_=0, to=100, orient="horizontal")
scale.pack()

button = tk.Button(root, text="Mostrar Valor", command=lambda: print("Valor:", scale.get()))
button.pack()

root.mainloop()
```

---

### **12. Scrollbar**
```python
import tkinter as tk

root = tk.Tk()
text = tk.Text(root, wrap="none", height=10)
text.pack(side="left", fill="both", expand=True)

scroll = tk.Scrollbar(root, command=text.yview)
scroll.pack(side="right", fill="y")
text.config(yscrollcommand=scroll.set)

for i in range(100):
    text.insert("end", f"Linha {i + 1}\n")

root.mainloop()
```

---

### **13. Text**
```python
import tkinter as tk

root = tk.Tk()
text = tk.Text(root, height=5, width=30)
text.pack()

button = tk.Button(root, text="Obter Texto", command=lambda: print("Texto:", text.get("1.0", "end-1c")))
button.pack()

root.mainloop()
```

---

### **14. Toplevel**
```python
import tkinter as tk

def abrir_janela():
    nova_janela = tk.Toplevel(root)
    nova_janela.title("Nova Janela")
    tk.Label(nova_janela, text="Essa é uma janela secundária!").pack()

root = tk.Tk()
button = tk.Button(root, text="Abrir Janela", command=abrir_janela)
button.pack()

root.mainloop()
```

---

## **Gerenciamento de Layout**

### **1. pack()**
```python
import tkinter as tk

root = tk.Tk()
tk.Label(root, text="Topo").pack(side="top")
tk.Label(root, text="Esquerda").pack(side="left")
tk.Label(root, text="Direita").pack(side="right")
root.mainloop()
```

---

### **2. grid()**
```python
import tkinter as tk

root = tk.Tk()
tk.Label(root, text="Linha 0, Coluna 0").grid(row=0, column=0)
tk.Label(root, text="Linha 0, Coluna 1").grid(row=0, column=1)
tk.Label(root, text="Linha 1, Coluna 0").grid(row=1, column=0)
root.mainloop()
```

---

### **3. place()**
```python
import tkinter as tk

root = tk.Tk()
tk.Label(root, text="Posição Absoluta").place(x=50, y=50)
root.geometry("200x200")
root.mainloop()
```

---

## **Eventos e Bindings**

### **bind()**
```python
import tkinter as tk

root = tk.Tk()
def ao_teclar(event):
    print(f"Tecla pressionada: {event.char}")

root.bind("<Key>", ao_teclar)
root.mainloop()
```

---
