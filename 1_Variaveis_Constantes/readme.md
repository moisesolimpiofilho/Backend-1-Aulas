# Variáveis
- Váriáveis são usadas para armazenar valores por exemplo:
  - Números inteiros
  - Números decimais
  - Informações textuais
  - Datas
  - Informações do tipo verdadeiro e falso

## Exemplos
Declarando variáveis sem definir os tipos das variáveis, neste caso os tipos são inferidos automaticamente pelo seu conteúdo.
```
nome = "Moisés"
idade = 41
peso = 87
altura = 1.65
estudando = True
maior_idade = False
```

Declarando variáveis definindo os tipos.
```
nome: str = "Moisés"
idade: int = 41
peso: int = 87
altura: float = 1.65
estudando: bool = True
maior_idade: bool = False
```

# Constantes
- Constantes no python são identificadas pela forma como são declaradas (escritas), por padrão da linguagem utiliza-se letras maiúsculas

## Exemplo
```
PI = 3.141516
```

# Comando print
- Usada para imprimir no console o resultado de algum cálculo ou uma variável
- Existem várias formas (sintaxe) de escrever esse comando, vamos usar a forma abaixo, pois é mais simples

```
nome = "Moisés"
idade = 41

print(f"Sou {nome}, tenho {idade} anos")
```