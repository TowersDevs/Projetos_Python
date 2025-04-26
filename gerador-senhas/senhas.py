import random
import string

def gerar_senha(tamanho, incluir_numeros_simbolos=True):
    if incluir_numeros_simbolos:
        caracteres = string.ascii_letters + string.digits + string.punctuation
    else:
        caracteres = string.ascii_letters

    return ''.join(random.choice(caracteres) for _ in range(tamanho))

while True:
    print("\n" + "*" * 50)
    print("🔐 Gerador de Senhas 🔐\n")
    print("1. Gerar senha com números, símbolos e letras.")
    print("2. Gerar senha apenas com letras.")
    print("3. Sair\n")
    print("*" * 50)

    opcao = input("\nEscolha uma opção: ")

    if opcao in ["1", "2"]:
        try:
            tamanho = int(input("Digite o tamanho da senha: "))
            quantidade = int(input("Digite a quantidade de senhas a serem geradas: "))

            print("\n🔑 Senhas Geradas:")
            for i in range(quantidade):
                senha_gerada = gerar_senha(tamanho, incluir_numeros_simbolos=(opcao == "1"))
                print(f"{i+1}. {senha_gerada}")

        except ValueError:
            print("❌ Erro: Digite um número válido!")

    elif opcao == "3":
        print("\n🚪 Saindo do programa...")
        break

    else:
        print("\n⚠️ Opção inválida! Escolha 1, 2 ou 3.")
