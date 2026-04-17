while True:
    numero = int(input("Digite um número inteiro entre 1 e 25 (0 para sair): "))

    if numero == 0:
        break

    if numero >= 1 and numero <= 25:
        for i in range(1, numero + 1):
            print("*" * i)
    else:
        print("Digite um valor entre 1 e 25.")