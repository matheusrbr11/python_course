seq1 = "abcdefghijklmnopqrstuvwxyz123456789"
seq2 = "abcdefghpjklmnopqrstuvwxyz123456789"

conjunto = enumerate(zip(seq1, seq2))

for indice, (a, b) in conjunto:
    if a != b:
        print(f"Intem Errado: {indice}")