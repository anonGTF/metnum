def seidel(a, x, b, err):
    n = len(a)

    for j in range(0, n):
        d = b[j]
        for i in range(0, n):
            if (j != i):
                d -= a[j][i] * x[i]
        temp = d / a[j][j]
        err[j] = abs(x[j] - temp)
        x[j] = temp
    return x


n = int(input('masukan ordo: '))
a = []
b = []
x = []
err = []

for i in range(0, n):
    temp = []
    x.append(0)
    err.append(999)
    for j in range(0, n):
        numb = int(input(f'masukan angka ke-{j+1} pers. ke-{i+1}: '))
        temp.append(numb)
    a.append(temp)
    numb = int(input(f'masukan result pers. ke-{i+1}: '))
    b.append(numb)

iterasi = int(input('masukan maksimal iterasi: '))
e = float(input('masukan error: '))
print(x)

for i in range(0, iterasi):
    x = seidel(a, x, b, err)
    print(x)
    if max(err) < e:
        break
