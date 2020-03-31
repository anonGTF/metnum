# inisialisasi ordo, dkk
baris = int(input("masukan ordo: "))
kolom = baris + 1

# inisialisasi matriks
main = []
for i in range(0, baris):
    temp = []
    for j in range(0, kolom):
        temp.append(0)
    main.append(temp)

# input komponen matriks
for i in range(0, baris):
    for j in range(0, kolom):
        main[i][j] = int(input(f"masukan angka ke-[{i}][{j}]: "))

# menjadikan diagonal utama == 1
for i in range(0, baris):
    pivot = main[i][i]
    for j in range(0, kolom):
        main[i][j] /= pivot

    # meng-0-kan di bawah diagonal utama
    for k in range(i + 1, kolom):
        if k != baris:
            pivot1 = main[k][i]
            for j in range(0, kolom):
                main[k][j] = main[k][j] - pivot1 * main[i][j]

for i in range(baris-1, -1, -1):
    for j in range(i-1, -1, -1):
        for k in range(baris, -1, -1):
            main[j][k] = main[j][k] - main[j][i]*main[i][k]

for i in range(0, baris):
    for j in range(0, kolom):
        print("%4.2f" % (main[i][j]), end=" ")
    print("\n")

# menampilkan output
for i in range(0, baris):
    print("x%d: %4.2f " % (i+1, main[i][baris]), end=" ")
