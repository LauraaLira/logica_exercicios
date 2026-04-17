while True:
    numero = int(input("Insira um número ímpar entre 3 e 35: "))

    if numero == 0:
        break

    if numero < 3 or numero > 35:
        print("Selecione um número entre 3 e 35")
    elif numero % 2 == 0:
        print("Selecione apenas numeors impares")
    else:
        largura = numero * 2 - 1
    
        for i in range(1, (numero // 2) + 2):
            esp = " " * ((largura - (2 * i - 1)) //  2)
            ast = "*" * (2 * i - 1)
            print(esp + ast)

        for i in range((numero // 2), 0, -1):
            espacos = " " * ((largura - (2 * i - 1)) // 2)
            asteriscos = "*" * (2 * i - 1)
            print(espacos + asteriscos)