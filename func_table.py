from func import *


def table(a, b, c, batas_atas, batas_bawah, iterasi):

    myfunc = MyFunc(a, b, c)
    x1 = batas_bawah
    h = (batas_atas - batas_bawah) / iterasi

    for j in range(0, iterasi):
        x2 = x1 + h
        y1 = myfunc.func(x1)
        y2 = myfunc.func(x2)
        print('x1: %6.4f x2: %6.4f f(x1): %6.4f f(x2): %6.4f ' % (x1, x2, y1, y2))
        if y1 * y2 <= 0:
            if abs(y1) < abs(y2):
                return x1
            else:
                return x2
        x1 = x2
