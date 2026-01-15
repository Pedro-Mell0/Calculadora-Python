import customtkinter as ctk

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.title("Calculadora")
app.geometry("400x650")

# Frame dos botões
frame = ctk.CTkFrame(app)
frame.pack(side="bottom", fill="x", pady=20)

# Display
display_frame = ctk.CTkFrame(app)
display_frame.pack(side="top", fill="x", padx=20, pady=20)

display = ctk.CTkEntry(
    display_frame,
    height=80,
    font=("Arial", 30),
    justify="right"
)
display.pack(fill="x", padx=10, pady=10)


#  FUNÇÕES 

def clicar(valor):
    if valor == 'C' or valor == 'CE':
        display.delete(0, 'end')

    elif valor == '⌫':
        texto = display.get()
        display.delete(0, 'end')
        display.insert(0, texto[:-1])

    elif valor == '=':
        try:
            resultado = eval(display.get())
            display.delete(0, 'end')
            display.insert(0, str(resultado))
        except:
            display.delete(0, 'end')
            display.insert(0, 'Erro')

    else:
        display.insert('end', valor)


#  BOTÕES 

botoes = [
    ['%', 'CE', 'C', '⌫'],
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['.', '0', '=', '+']
]

for linha, row in enumerate(botoes):
    for coluna, valor in enumerate(row):
        ctk.CTkButton(
            frame,
            text=valor,
            font=("Arial", 20),
            width=80,
            height=80,
            command=lambda v=valor: clicar(v)
        ).grid(row=linha, column=coluna, padx=10, pady=10)


# Executar aplicação
app.mainloop()