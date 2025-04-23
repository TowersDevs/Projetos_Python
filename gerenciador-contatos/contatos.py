agenda = []

while True:
    print("---------------------------------")
    print("📱 Gerenciador de Contatos \n")
    print("1. Adicionar contato")
    print("2. Listar contatos")
    print("3. Buscar contato")
    print("4. Remover contato")
    print("5. Sair")
    print("---------------------------------")
    opcao = input("Escolha uma opção: ")
    print("---------------------------------")
    
    if opcao == "1":
        nome = input("\nDigite o nome do contato: ")
        telefone = input("Digite o número de telefone: ")

        contato = {
            "nome": nome,
            "telefone": telefone,
        }

        agenda.append(contato)
        print("\nContato adicionado com sucesso!\n")


    elif opcao == "2":
        if not agenda:
            print("\n📌 Lista de contatos está vazia!\n")
        else:
            print("\nLista de contatos:\n")
            for contato in agenda:
              print(f"{contato['nome']}: {contato['telefone']}\n")

    elif opcao == "3":
        nome = input("Digite o nome do contato que deseja buscar: ")
        encontrado = False
        for contato in agenda:
            if contato["nome"] == nome:
                print(f"{contato['nome']}: {contato['telefone']}\n")
                encontrado = True
                break
        if not encontrado:
          print("Contato não encontrado.")

    elif opcao == "4":
        nome = input("Digite o nome do contato que deseja remover: ")
        for i, contato in enumerate(agenda):
            if contato["nome"].lower() == nome.lower():
                del agenda[i]
                print("Contato removido com sucesso!\n")
                break
        else:
            print("Contato não encontrado.")

    elif opcao == "5":
        print("\nSaindo do programa...")
        break

    else:
        print("\nOpção inválida! Por favor, escolha uma opção válida.\n")
