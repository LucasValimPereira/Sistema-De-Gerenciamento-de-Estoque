estoque = {}

while True:
    print("\n1 - Entrda de produto")
    print("2 - Saída de produto")
    print("3 - Ver estoque")
    print("4 - Sair")

    opcao = input("Escolha uma opção:")

    if opcao == "1":
        produto = input("Produto: ").lower()
        qtd = int(input("Quantidade de entrada: "))

        if produto in estoque:
            estoque[produto] += qtd
        else:
            estoque[produto] = qtd

        print("Estoque atualizado!")

    elif opcao == "2":
        produto = input("Produto: "). lower()
        qtd = int(input("Quantidade de saída: "))

        if produto in estoque and estoque[produto] >= qtd:
            estoque[produto] -= qtd
            print("Saída registrada!")
        else:
            print("Produto não encontrado ou quantidade insuficiente em estoque.")

    elif opcao == "4":
        print("Sistema encerrado")
        break