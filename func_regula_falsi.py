from func import *


def regula_falsi(a, b, c, batas_bawah, batas_atas, error, iterasi):

    myfunc = MyFunc(a, b, c)

    err = 100000
    i = 0
    f_bawah = myfunc.func(batas_bawah)
    f_atas = myfunc.func(batas_atas)

    while i < iterasi and err > error:
        x = myfunc.nilaix(batas_bawah, batas_atas)
        fx = myfunc.func(x)
        err = abs(fx)
        if f_bawah * fx < 0:
            batas_atas = x
            f_atas = fx
        elif fx * f_atas < 0:
            batas_bawah = x
            f_bawah = fx

    return x
