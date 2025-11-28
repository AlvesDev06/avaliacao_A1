# Sistema Multi-Funções Python

Um sistema simples em Python que oferece múltiplas funcionalidades em um único programa, sem o uso de funções definidas pelo usuário.

## Funcionalidades

### 1. Cadastro de Produtos
Permite cadastrar produtos com seus respectivos preços em um dicionário. O usuário pode adicionar vários produtos até digitar "sair" no nome do produto. Ao final, exibe todos os produtos cadastrados com seus preços formatados.

**Como executar:**
- Escolha a opção 1 no menu principal.
- Digite o nome do produto e pressione Enter.
- Digite o preço do produto e pressione Enter.
- Repita até digitar "sair" no nome do produto.

**Exemplo de entrada:**
```
1
Caneta
2.50
Caderno
10.00
sair
```

**Exemplo de saída:**
```
Produtos cadastrados:
----------------------------------------------------
Produto: Caneta | Preço: R$ 2.50
Produto: Caderno | Preço: R$ 10.00
----------------------------------------------------
```

### 2. Mostrar Números Pares até 100
Exibe todos os números pares de 1 a 100 usando um laço `while`.

**Como executar:**
- Escolha a opção 2 no menu principal.

**Exemplo de saída:**
```
Contador de números pares até 100:
2
4
6
8
...
100
Fim do programa.
```

### 3. Verificação de Idade
Solicita a idade do usuário e verifica se a entrada é permitida com base na idade:
- 18 anos ou mais: entrada permitida.
- 16 ou 17 anos: entrada permitida com acompanhante.
- Menos de 16 anos: entrada negada.

**Como executar:**
- Escolha a opção 3 no menu principal.
- Digite sua idade.

**Exemplo de entrada:**
```
3
20
```

**Exemplo de saída:**
```
Entrada permitida! Você é maior de idade.
Obrigado por utilizar o sistema!
-------------------------------------------
```

### 4. Cadastro de Alunos
Permite cadastrar nomes de alunos em uma lista. O usuário pode adicionar vários alunos até digitar "sair". Ao final, exibe todos os alunos cadastrados.

**Como executar:**
- Escolha a opção 4 no menu principal.
- Digite o nome do aluno e pressione Enter.
- Repita até digitar "sair".

**Exemplo de entrada:**
```
4
Maria
João
Ana
sair
```

**Exemplo de saída:**
```
Lista de alunos cadastrados:
----------------------------------------------------
Maria
João
Ana
----------------------------------------------------
```

### 5. Sair
Encerra o sistema.

## Como Executar o Programa

1. Salve o código em um arquivo com extensão `.py`.
2. Execute o arquivo usando o interpretador Python: `python nome_do_arquivo.py`.
3. Escolha uma opção do menu principal digitando o número correspondente e pressionando Enter.

## Observações

- O programa utiliza estruturas de repetição (`while`), condicionais (`if`, `elif`, `else`), e estruturas de dados como dicionários e listas.
- Não utiliza funções definidas pelo usuário, conforme solicitado.
