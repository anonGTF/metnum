from menu import *


print("ax^2 + bx + c\n")
a = float(input("masukan nilai a: "))
b = float(input("masukan nilai b: "))
c = float(input("masukan nilai c: "))

print(f"\nfungsi: ({a})x^2 + ({b})x + ({c})\n")

menu = Menu(a, b, c, None, None, None, None, None)

print("\nMenu Metode Penyelesaian:\n"
      "1. Metode table\n"
      "2. Metode biseksi\n"
      "3. Metode regula falsi\n"
      "4. Metode iterasi sederhana\n"
      "5. Metode Newton Raphson\n"
      "6. Metode Secant\n")

pilihan_metode = int(input("masukan pilihan: "))

print(f'\nhasil: {menu.pilihan(menu, pilihan_metode)}')