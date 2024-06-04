"""
Crie um script que gere um numero aleatório de 1 até 20
o usuário precisa acertar o número, enquanto não
acertar fica dentro da repetição
"""

import random

while True:
    numero_sorteado = random.randint(1, 20)
    numero_usuario = int(input("Digite um número inteiro: "))

    if numero_usuario == numero_sorteado:
        print(f"Parabéns você acertou o número {numero_sorteado}")
        continuar = input("Deseja continuar? (s/n)")

        if continuar == "n":
            break
    else:
        print(f"Você errou o número sorteado foi {numero_sorteado}")