"""
Exemplo de script que faz a verificação do ano do veículo
"""

from datetime import date

hoje = date.today()
ano = hoje.year

ano_carro = int(input("Digite o ano do carro: "))

idade_carro = ano - ano_carro

if idade_carro > 20:
    print(f"O carro tem mais que 20 anos, a idade é {idade_carro}")
else:
    print(f"O carro tem menos que 20 anos, a idade é {idade_carro}")