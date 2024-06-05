

def gerar():
    numero = numero_input.get()

    label1.config(text=f"1 X {numero} = {1 * numero}")
    print(f"Gerar tabuada para numero {numero}")



from tkinter import Tk, Frame, Entry, Button, Label, messagebox

# Configuração inicial da janela
janela = Tk()
janela.title("Gerador de Tabuada")
janela.geometry(f"{400}x{500}")
janela.configure(bg="yellow")

# Borda opções: ridge, flat, sunken, raised, groove
frm = Frame(janela, borderwidth=25, width=350, height=480, bg="black")  # relief='ridge', bg="white",
frm.place(relx=0.5, rely=0.5, anchor='center')  # Centraliza o frame na janela

# Desabilita a propagação de tamanho do frame
frm.grid_propagate(False)

font_config = ("Arial", 16)
pad_config = 5

numero_input = Entry(frm, font=font_config, width=10)
numero_input.grid(column=0, row=0, padx=15)
Button(frm, text="Gerar", font=font_config, command=gerar).grid(column=1, row=0)

label1 = Label(frm, text="1 X ? = ", font=font_config)
label1.grid(column=0, row=1, pady=pad_config)

label2 = Label(frm, text="2 X ? = ", font=font_config)
label2.grid(column=0, row=2, pady=pad_config)

label3 =Label(frm, text="3 X ? = ", font=font_config)
label3.grid(column=0, row=3, pady=pad_config)

label4 = Label(frm, text="4 X ? = ", font=font_config)
label4.grid(column=0, row=4, pady=pad_config)

label5 = Label(frm, text="5 X ? = ", font=font_config)
label5.grid(column=0, row=5, pady=pad_config)

label6 = Label(frm, text="6 X ? = ", font=font_config)
label6.grid(column=0, row=6, pady=pad_config)

label7 = Label(frm, text="7 X ? = ", font=font_config)
label7.grid(column=0, row=7, pady=pad_config)

label8 = Label(frm, text="8 X ? = ", font=font_config)
label8.grid(column=0, row=8, pady=pad_config)

label9 = Label(frm, text="9 X ? = ", font=font_config)
label9.grid(column=0, row=9, pady=pad_config)

label10 = Label(frm, text="10 X ? = ", font=font_config)
label10.grid(column=0, row=10, pady=pad_config)

janela.mainloop()