print("-" * 20)
print("CAIXA ELETRÔNICO")
print("-" * 20)

while True:
    senha = (input("Digite a senha de seu cartão: "))
    if senha != "1234":
        print("Senha incorreta.")
        break
    else:
        print("ACESSO AUTORIZADO!\n")
        print("-" * 20)
        print("SAQUE: \n")
        print("[1] R$ 10,00\n")
        print("[2] R$ 20,00\n")
        print("[3] R$ 30,00\n")
        print("[4] R$ 40,00\n")
        print("[5] R$ 50,00\n")
        opt = input("Selecione uma opção (número) de saque: ")
        if opt == "1":
            print("Você fez um saque de R$10,00")
            break
        elif opt == "2":
            print("Você fez um saque de R$20,00")
            break
        elif opt == "3":
            print("Você fez um saque de R$30,00")
            break
        elif opt == "4":
            print("Você fez um saque de R$40,00")
            break
        else:
            print("Você fez um saque de R$50,00")

