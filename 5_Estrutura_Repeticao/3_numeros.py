"""
Crie um script que mostre os numeros do início até 
o fim, sendo que os números devem ser escolhidos pelo usuário.
Também o usuário deve selecionar o passo dos números
"""

inicio = int(input("Digite um número para iniciar: "))
fim = int(input("Digite um número para parar: "))
passo = int(input("Digite o passo dos números: "))

for numero in range(inicio, fim+1, passo):
    print(f"O número é {numero}")
