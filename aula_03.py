sentence = input("Please, enter a sentence: ")

for char in sentence:
    decimal = ord(char)
    binary = format(decimal, "08b")

    if char == " ":
        decimal = 0
        binary = "00000000"
    
    print(f"Char '{char} -> Decimal: {decimal:>3}' -> Binary: {binary}")