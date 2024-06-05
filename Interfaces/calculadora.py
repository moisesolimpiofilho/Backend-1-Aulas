
visor = ""
numeros = []
operacao = ""

def click_botao(numero):
    """
    Função que recebe o número clicado
    """
    global visor, numeros

    visor += str(numero)
    numeros.append(numero)
    display.config(text=visor)

    if len(numeros) == 2:
        calcular()


def click_operacao(op):
    """
    Função que recebe a operação que foi clicada
    """
    global visor, operacao

    if op == "+" or op == "-" or op == "X" or op == "/":
        visor += str(op)
        operacao = op
        display.config(text=visor)
        

def calcular():
    """
    Função que realiza o cálculo conforme os dois números 
    e a operação selecionada
    """
    global numeros, operacao

    numero1 = numeros[0]
    numero2 = numeros[1]
    resultado = 0

    if operacao == "+":
        resultado = numero1 + numero2
    elif operacao == "-":
        resultado = numero1 - numero2
    elif operacao == "X":
        resultado = numero1 * numero2
    elif operacao == "/":
        resultado = numero1 / numero2

    messagebox.showinfo("Resultado", f"{resultado}")
    click_limpar()
    
    
def click_limpar():
    """
    Função que limpa o display da calculadora
    """
    global numeros, operacao, visor

    display.config(text="")
    visor = ""
    numeros.clear()
    operacao = ""



"""
O código abaixo cria a tela da Calculadora
Por enquanto não precisa mexer nesta parte
"""

from tkinter import Tk, Frame, Button, Label, messagebox

# Configuração inicial da janela
janela = Tk()
janela.title("Calculadora")
janela.geometry(f"{400}x{450}")
janela.configure(bg="yellow")

# Borda opções: ridge, flat, sunken, raised, groove
frm = Frame(janela, borderwidth=25, width=350, height=430, bg="black")  # relief='ridge', bg="white",
frm.place(relx=0.5, rely=0.5, anchor='center')  # Centraliza o frame na janela

# Desabilita a propagação de tamanho do frame
frm.grid_propagate(False)

font_config = ("Arial", 16)
pad_config = 5
w_btn = 5
h_btn = 2
pd_btn = 2

# Configura o visor
display = Label(frm, text="0", font=font_config, width=24, height=2, bg="white", anchor="e")
display.grid(column=0, row=0, columnspan=4, padx=0, pady=pd_btn)

# Configura os botões
Button(frm, text="7", font=font_config, width=w_btn, height=h_btn, command=lambda: click_botao(7)).grid(column=0, row=1, padx=pd_btn, pady=pd_btn)
Button(frm, text="8", font=font_config, width=w_btn, height=h_btn, command=lambda: click_botao(8)).grid(column=1, row=1, padx=pd_btn, pady=pd_btn)
Button(frm, text="9", font=font_config, width=w_btn, height=h_btn, command=lambda: click_botao(9)).grid(column=2, row=1, padx=pd_btn, pady=pd_btn)
Button(frm, text="X", font=font_config, width=w_btn, height=h_btn, command=lambda: click_operacao("X")).grid(column=3, row=1, padx=pd_btn, pady=pd_btn)

Button(frm, text="4", font=font_config, width=w_btn, height=h_btn, command=lambda: click_botao(4)).grid(column=0, row=2, padx=pd_btn, pady=pd_btn)
Button(frm, text="5", font=font_config, width=w_btn, height=h_btn, command=lambda: click_botao(5)).grid(column=1, row=2, padx=pd_btn, pady=pd_btn)
Button(frm, text="6", font=font_config, width=w_btn, height=h_btn, command=lambda: click_botao(6)).grid(column=2, row=2, padx=pd_btn, pady=pd_btn)
Button(frm, text="-", font=font_config, width=w_btn, height=h_btn, command=lambda: click_operacao("-")).grid(column=3, row=2, padx=pd_btn, pady=pd_btn)

Button(frm, text="1", font=font_config, width=w_btn, height=h_btn, command=lambda: click_botao(1)).grid(column=0, row=3, padx=pd_btn, pady=pd_btn)
Button(frm, text="2", font=font_config, width=w_btn, height=h_btn, command=lambda: click_botao(2)).grid(column=1, row=3, padx=pd_btn, pady=pd_btn)
Button(frm, text="3", font=font_config, width=w_btn, height=h_btn, command=lambda: click_botao(3)).grid(column=2, row=3, padx=pd_btn, pady=pd_btn)
Button(frm, text="+", font=font_config, width=w_btn, height=h_btn, command=lambda: click_operacao("+")).grid(column=3, row=3, padx=pd_btn, pady=pd_btn)

Button(frm, text=",", font=font_config, width=w_btn, height=h_btn).grid(column=0, row=4, padx=pd_btn, pady=pd_btn)
Button(frm, text="0", font=font_config, width=w_btn, height=h_btn, command=lambda: click_botao(0)).grid(column=1, row=4, padx=pd_btn, pady=pd_btn)
Button(frm, text="=", font=font_config, width=w_btn, height=h_btn, command=lambda: click_operacao("=")).grid(column=2, row=4, padx=pd_btn, pady=pd_btn)
Button(frm, text="/", font=font_config, width=w_btn, height=h_btn, command=lambda: click_operacao("/")).grid(column=3, row=4, padx=pd_btn, pady=pd_btn)

Button(frm, text="Limpar", font=font_config, width=24, height=h_btn, command=click_limpar).grid(column=0, row=5, columnspan=5, padx=pd_btn, pady=pd_btn)

janela.mainloop()
