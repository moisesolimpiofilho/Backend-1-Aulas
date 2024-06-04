"""
Crie um algoritmo que verifique se a pessoa pode ir à
sorveteria ao final de semana, para que isso aconteça
o dia deve estar ensolarado e a pessoa precisa ter pelo menos R$ 20,00.
"""

nome = input("Digite seu nome: ")
idade = int(input("Qual sua idade? "))
ensolarado = input("Hoje o dia está ensolarado? ")
dinheiro = float(input("Quanto você tem de dinheiro? "))

if idade >= 18 and ensolarado == "sim" and dinheiro >= 20.00:
    print(f"Olá {nome}, hoje está um lindo dia ensolarado, "
          f"você vai à sorveteria e possui R$ {dinheiro} para gastar")
else:
    print("Você não vai a sorveteria")
