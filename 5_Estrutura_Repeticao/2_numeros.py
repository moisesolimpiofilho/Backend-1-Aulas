"""
Crie um script que mostre os numeros do início até 
o fim, sendo que os números devem ser escolhidos pelo usuário
"""

inicio = int(input("Digite um número para iniciar: "))
fim = int(input("Digite um número para parar: "))

for numero in range(inicio, fim+1):
    print(f"O número é {numero}")
