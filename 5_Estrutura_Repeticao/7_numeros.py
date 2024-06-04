"""
Crie um script que mostre os numeros de 0 até 
um número escolhido pelo usuário usando while
"""

numero_usuario = int(input("Digite um número inteiro: "))
contador = 0

while contador <= numero_usuario:
    print(f"O número é {contador}")
    contador += 1
