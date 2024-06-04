"""
Calcule a média aritmética de duas notas do aluno.
As informações devem ser inseridas pelo usuário
"""

aluno = input("Qual nome do aluno? ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

print(f"O aluno {aluno} teve duas notas {nota1}, {nota2}, e sua média foi {media}")
