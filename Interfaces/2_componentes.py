from tkinter import *
from tkinter import ttk

def on_button_click():
    print("Botão clicado!")

root = Tk()
root.title("Minha Interface Expansível")

frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

# Entry
ttk.Label(frm, text="Digite algo:").grid(column=0, row=1)
ttk.Entry(frm).grid(column=1, row=1)

# Combobox
ttk.Label(frm, text="Escolha uma opção:").grid(column=0, row=2)
combobox = ttk.Combobox(frm, values=["Opção 1", "Opção 2", "Opção 3"])
combobox.grid(column=1, row=2)

# Checkbox
chk_var = BooleanVar()
chk = ttk.Checkbutton(frm, text="Marque-me", variable=chk_var)
chk.grid(column=0, row=3)

# Radio Buttons
radio_var = StringVar()
ttk.Radiobutton(frm, text="Opção A", variable=radio_var, value="A").grid(column=0, row=4)
ttk.Radiobutton(frm, text="Opção B", variable=radio_var, value="B").grid(column=1, row=4)

# Botão com funcionalidade
ttk.Button(frm, text="Clique Aqui", command=on_button_click).grid(column=0, row=5)

root.mainloop()
