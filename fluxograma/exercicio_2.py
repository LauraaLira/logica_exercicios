print("-" * 30)
print("SISTEMA DE VALIDAÇÃO DE NOTAS")
print("-" * 30)

nome = input("Insira o nome do aluno: ")
n1 = float(input("Insira a primeira nota: "))
n2 = float(input("Insira a segunda nota: "))
media = (n1 + n2) / 2

if media >= 7:
    print(f"Aluno: {nome} foi aprovado")
    print(f"Sua média foi {media}")
else:
    print(f"Aluno: {nome} foi reprovado.")
    print("Exame final.")
    print(f"Sua média foi {media}")

