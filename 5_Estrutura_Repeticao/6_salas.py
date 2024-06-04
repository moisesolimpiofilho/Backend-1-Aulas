"""
Crie um script que lista as salas da escola
e número pelo índice do item da lista
"""

salas = [
    "Sala desenho", "Sala gerais 01", "Sala gerais 02",
    "Sala AutoCAD", "Sala CLP", "Sala mecânica"
]

for index, sala in enumerate(salas):
    print(f"{index} - {sala}")