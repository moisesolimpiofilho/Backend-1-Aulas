"""
Exemplo de script que solicita ao usuário
suas informações pessoais
"""

nome = input("Qual seu nome? ")
idade = int(input("Qual sua idade? "))
peso = int(input("Qual seu peso? "))
altura = float(input("Qual sua altura? "))

print(f"Sou {nome}, tenho {idade} anos")
print(f"Meu peso é {peso} e altura {altura}")