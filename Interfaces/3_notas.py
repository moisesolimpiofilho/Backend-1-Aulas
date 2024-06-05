from tkinter import Tk, Frame, Label, Button, Entry

def calcular_nota():
    aluno = aluno_input.get()
    nota1 = float(nota1_input.get())
    nota2 = float(nota2_input.get())

    media = (nota1 + nota2) / 2

    media_label.config(text=f"A média é: {media:.2f}")

# Configuração inicial da janela
janela = Tk()
janela.title("Cálculo de notas")
janela.geometry(f"{400}x{300}")
janela.configure(bg="lightblue")

# Borda opções: ridge, flat, sunken, raised, groove
frm = Frame(janela, borderwidth=25, width=350, height=280)  # relief='ridge', bg="white",
frm.place(relx=0.5, rely=0.5, anchor='center')  # Centraliza o frame na janela

# Desabilita a propagação de tamanho do frame
frm.grid_propagate(False)

font_config = ("Arial", 14)
pad_config = 5

Label(frm, text="Preencha as informações", font=font_config).grid(column=0, row=0, padx=pad_config, pady=pad_config, columnspan=2)

Label(frm, text="Aluno", font=font_config).grid(column=0, row=1, padx=pad_config, pady=pad_config)
aluno_input = Entry(frm, font=font_config)
aluno_input.grid(column=1, row=1, padx=pad_config, pady=pad_config)

Label(frm, text="Nota 1", font=font_config).grid(column=0, row=2, padx=pad_config, pady=pad_config)
nota1_input = Entry(frm, font=font_config)
nota1_input.grid(column=1, row=2, padx=pad_config, pady=pad_config)

Label(frm, text="Nota 2", font=font_config).grid(column=0, row=3, padx=pad_config, pady=pad_config)
nota2_input = Entry(frm, font=font_config)
nota2_input.grid(column=1, row=3, padx=pad_config, pady=pad_config)

media_label = Label(frm, text="A média é: ", font=font_config)
media_label.grid(column=0, row=4, columnspan=2)

Button(frm, text="Calcular", font=font_config, command=calcular_nota).grid(column=0, row=5, columnspan=2, pady=20)

janela.mainloop()