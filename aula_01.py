import itertools

def tabela_verdade():
    print("Tabela Verdade para S = (A ^ B ) v (-C ^ D)")
    print("=" * 42)
    print("A\tB\tC\tD\ts")
    print("-" * 36)

    for A, B, C, D in itertools.product([False, True], repeat=4):
        S = (A and B) or (not C and D)
        print(f"{int(A)}\t{int(B)}\t{int(C)}\t{int(D)}\t{int(S)}")

tabela_verdade()