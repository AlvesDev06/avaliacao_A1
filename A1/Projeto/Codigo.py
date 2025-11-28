# ============================================
# SISTEMA MULTI-FUNÇÕES 
# ============================================

print("============================================")
print("        SISTEMA MULTI-FUNÇÕES PYTHON        ")
print("============================================")

# Variáveis principais
produtos = {}   # Para cadastro de produtos
alunos = []     # Para cadastro de alunos

while True:
    print("\n====== MENU PRINCIPAL ======")
    print("1 - Cadastro de produtos")
    print("2 - Mostrar números pares até 100")
    print("3 - Verificação de idade")
    print("4 - Cadastro de alunos")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    # ============================================
    # 1) CADASTRO DE PRODUTOS (DICIONÁRIO)
    # ============================================
    if opcao == "1":
        print("----------------------------------------------------")
        print("Cadastro de produtos (digite 'sair' no nome para encerrar)")

        while True:
            nome = input("Digite o nome do produto: ")

            if nome.lower() == "sair":
                break

            preco = float(input(f"Digite o preço de '{nome}': "))
            produtos[nome] = preco

        print("\nProdutos cadastrados:")
        print("----------------------------------------------------")
        for nome, preco in produtos.items():
            print(f"Produto: {nome}  |  Preço: R$ {preco:.2f}")
        print("----------------------------------------------------")


    # ============================================
    # 2) EXIBIR NÚMEROS PARES DE 1 A 100 (WHILE)
    # ============================================
    elif opcao == "2":
        print("\nContador de números pares até 100:")
        numero = 1

        while numero <= 100:
            if numero % 2 == 0:
                print(numero)
            numero += 1

        print("Fim do programa.")


    # ============================================
    # 3) VERIFICAÇÃO DE IDADE (IF / ELIF / ELSE)
    # ============================================
    elif opcao == "3":
        print("-------------------------------------------")
        idade = int(input("Digite sua idade: "))
        print("-------------------------------------------")

        if idade >= 18:
            print("Entrada permitida! Você é maior de idade.")
        elif idade >= 16:
            print("Entrada permitida somente com acompanhante.")
        else:
            print("Entrada negada. Você é menor de 16 anos.")

        print("Obrigado por utilizar o sistema!")
        print("-------------------------------------------")


    # ============================================
    # 4) CADASTRO DE ALUNOS (LISTA)
    # ============================================
    elif opcao == "4":
        print("----------------------------------------------------")
        print("Cadastro de alunos (digite 'sair' para encerrar)")

        while True:
            nome = input("Digite o nome do aluno: ")

            if nome.lower() == "sair":
                break

            alunos.append(nome)

        print("\nLista de alunos cadastrados:")
        print("----------------------------------------------------")
        for aluno in alunos:
            print(aluno)
        print("----------------------------------------------------")


    # ============================================
    # 5) SAIR DO SISTEMA
    # ============================================
    elif opcao == "5":
        print("Encerrando o sistema... Obrigado por usar!")
        break

    else:
        print("Opção inválida! Tente novamente.")

