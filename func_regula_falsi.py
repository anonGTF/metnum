from func import *


def regula_falsi(a, b, c, batas_atas, batas_bawah, error, iterasi):

    myfunc = MyFunc(a, b, c)

    err = 100000
    i = 0
    f_bawah = myfunc.func(batas_bawah)
    f_atas = myfunc.func(batas_atas)

    while i < iterasi and err > error:
        x = myfunc.nilaix(batas_bawah, batas_atas)
        fx = myfunc.func(x)
        err = abs(fx)
        print('bb: %6.4f ba: %6.4f x: %6.4f f(bb): %6.4f f(bb): %6.4f f(x): %6.4f ' % (batas_bawah, batas_atas, x, f_bawah, f_atas, fx))
        if f_bawah * fx < 0:
            batas_atas = x
            f_atas = fx
        elif fx * f_atas < 0:
            batas_bawah = x
            f_bawah = fx

    return x
