from func_table import *
from func_bisection import *
from func_regula_falsi import *
from func_iterasi import *
from func_newton_raphson import *
from func_secant import *


class Menu:
    def __init__(self, a, b, c, batas_bawah, batas_atas, iterasi, error, tebakan):
        self.a = a
        self.b = b
        self.c = c
        self.batas_atas = batas_atas
        self.batas_bawah = batas_bawah
        self.iterasi = iterasi
        self.error = error
        self.tebakan = tebakan

    def input_met_1(self, menu):
        menu.batas_bawah = int(input("\nmasukan batas bawah: "))
        menu.batas_atas = int(input("masukan batas atas: "))
        menu.iterasi = int(input("masukan maksimal iterasi: "))
        menu.error = float(input("masukan error: "))
        return menu

    def input_met_2(self, menu):
        menu.tebakan = int(input("\nmasukan tebakan awal: "))
        menu.error = float(input("masukan error: "))
        return menu

    def pilihan(self, menu, x):
        if x == 1:
            menu.input_met_1(menu)
            return table(self.a, self.b, self.c, self.batas_atas, self.batas_bawah, self.iterasi)
        elif x == 2:
            menu.input_met_1(menu)
            return bisection(self.a, self.b, self.c, self.batas_atas, self.batas_bawah, self.error)
        elif x == 3:
            menu.input_met_1(menu)
            return regula_falsi(self.a, self.b, self.c, self.batas_atas, self.batas_bawah, self.error, self.iterasi)
        elif x == 4:
            menu.input_met_2(menu)
            return iterasi(self.a, self.b, self.c, self.tebakan, self.error)
        elif x == 5:
            menu.input_met_2(menu)
            return newton_raphson(self.a, self.b, self.c, self.tebakan, self.error)
        elif x == 6:
            menu.input_met_1(menu)
            return secant(self.a, self.b, self.c, self.batas_bawah, self.batas_atas, self.error)