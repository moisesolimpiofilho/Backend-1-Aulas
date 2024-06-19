# Estrutura de decisão
- São usadas para direcionar o fluxo dentro do algoritmo
- Em python temos algumas considerações a respeito, vejamos um exemplo:

## Exemplo

```
if n1 > n2:
    print(f"O primeiro número {n1} é maior que segundo número {n2}")
if n2 > n1:
    print(f"O segundo número {n2} é maior que o primeiro número {n1}")
```

**Pontos importantes**
- Não usamos chaves "{ }" para delimitar a estrutura de decisão.
- Ao final da condição a ser avaliada precisa coloca os dois pontos ":"
- Em python usamos a tabulação (espaços) para saber que um código pertence dentro de um if.
- Essa tabulação é feita com a tecla "tab" do teclado ou 4 espaços com a barra de espaços.

# Exemplo com if e else
```
if idade_carro > 20:
    print(f"O carro tem mais que 20 anos, a idade é {idade_carro}")
else:
    print(f"O carro tem menos que 20 anos, a idade é {idade_carro}")
```

**Pontos importantes**
- Ao final do else precisa coloca os dois pontos ":"

# Exemplo com if, else e elif
```
if minutos <= 200:
    valor_conta = minutos * 0.20
elif minutos > 200:
    valor_conta = minutos * 0.18
```

**Pontos importantes**
- Ao final da condição a ser avaliada precisa coloca os dois pontos ":"

# Operadores lógicos
- Em python temos os operadores lógicos **and** e **or**.
- São utilizados dentro das estruturas de decisão quando queremos avaliar mais de uma condição.

# Exemplo de if com operadores lógicos 
```
if idade >= 18 and ensolarado == "sim" and dinheiro >= 20.00:
    print("Você vai à sorveteria")
else:
    print("Você não vai à sorveteria")
```