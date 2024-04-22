"""
Algoritmo que calcula o valor do produto conforme sua categoria
1 -> 10,00
2 -> 18,00
3 -> 23,00
4 -> 26,00
5 -> 31,00 
"""

categoria = int(input("Digite a categoria do produto: "))
qtde = int(input("Digite a quantidade a ser comprada: "))

valor_produto = 0.0

if categoria == 1:
    valor_produto = qtde * 10
elif categoria == 2:
    valor_produto = qtde * 18
elif categoria == 3:
    valor_produto = qtde * 23
elif categoria == 4:
    valor_produto = qtde * 26
elif categoria == 5:
    valor_produto = qtde * 31

print(f"O valor a ser pago é R$ {valor_produto:.2f} para categoria {categoria}")
