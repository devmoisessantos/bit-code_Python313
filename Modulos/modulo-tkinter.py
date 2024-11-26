# MODULO TKINTER:
"""
- O modulo tkinter possui diversas funcoes para trabalhar com interface gráfica
- Ex: criacao de janelas, botoes, etc...

É bastante utilizado para trabalhar com interface gráfica, por exemplo:
Criar programas gráficos e interfaces de usuário.

"""
import tkinter as tk

def clicar():
    label.config(text=entrada.get())

janela = tk.Tk()
janela.geometry('300x150')
janela.title('Gerenciadoe de Frase')


frame = tk.Frame(janela)
frame.pack(padx=10, pady=10, fill='x', expand=True)

label = tk.Label(frame, text='Ola, Mundo!')
label.pack(fill='x', expand=True)



label = tk.Label(frame, text='Digite uma frase:')
label.pack(fill='x', expand=True)


entrada = tk.Entry(frame)
entrada.pack(fill='x', expand=True)



botao = tk.Button(janela, text='Enviar', command= clicar)
botao.pack()



janela.mainloop()