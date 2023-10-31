baris = int(input("Masukkan jumlah baris: "))

for bntg in range(1, baris + 1):
    for br in range(bntg):
        print("*", end="")
    print()