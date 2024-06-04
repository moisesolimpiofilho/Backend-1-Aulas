"""
Crie um script que mostre os numeros de 0 até 
um número escolhido pelo usuário
"""

numero_usuario = int(input("Digite um número inteiro: "))

for numero in range(numero_usuario+1):
    print(f"O número é {numero}")
