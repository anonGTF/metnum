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

for i in range(0, baris):
    for j in range(0, kolom):
        print("%4.2f" % (main[i][j]), end=" ")
    print("\n")

# menghitung nilai x1, x2, x3

x3 = main[2][3]
x2 = main[1][3] - main[1][2]*x3
x1 = main[0][3] - main[0][2]*x3 - main[0][1]*x2

# menampilkan output
print("x1: %4.2f x2: %4.2f x3: %4.2f" % (x1, x2, x3))

# for i in range(0, 3):
#     for j in range(0, 4):
#         print(main[i][j], end=" ")
#     print("\n")
