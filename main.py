import customtkinter as ctk

ctk.set_appearance_mode('dark')
def validar():
    senha = input_senha.get()
    nome = input_nome.get()
    if nome == 'vitor' and senha == "1234":
        print("login validado")
    else:
        print("login não validado")
janela = ctk.CTk()
janela.title('sistema de login teste')
janela.geometry('300x300')

campo_nome = ctk.CTkLabel(janela,text='Seu nome')
campo_nome.pack(pady=20)

input_nome = ctk.CTkEntry(janela,placeholder_text='digite seu nome')
input_nome.pack()
campo_nome = ctk.CTkLabel(janela,text='Sua senha')
campo_nome.pack(pady=20)

input_senha = ctk.CTkEntry(janela,placeholder_text='digite sua senha')
input_senha.pack()
login = ctk.CTkButton(janela,text='logar',command=validar)
login.pack(pady=10)



janela.mainloop()