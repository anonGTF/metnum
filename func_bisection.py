from func import *


def bisection(a, b, c, batas_atas, batas_bawah, error, iterasi):
    myfunc = MyFunc(a, b, c)

    i = 0
    tengah = (batas_atas + batas_bawah) / 2

    while (tengah - batas_bawah) > error and i < iterasi:
        tengah = (batas_atas + batas_bawah) / 2
        y_bawah = myfunc.func(batas_bawah)
        y_tengah = myfunc.func(tengah)
        y_atas = myfunc.func(batas_atas)
        print('a: %6.4f b: %6.4f c: %6.4f ya: %6.4f yb: %6.4f yc: %6.4f ' % (batas_bawah, tengah, batas_atas, y_bawah, y_tengah, y_atas))
        if y_bawah * y_tengah < 0:
            batas_atas = tengah
        elif y_tengah * y_atas < 0:
            batas_bawah = tengah
        tengah = (batas_atas + batas_atas) / 2
        i += 1

    y_bawah = myfunc.func(batas_bawah)
    y_tengah = myfunc.func(tengah)

    if abs(y_bawah) < abs(y_tengah):
        return batas_bawah
    else:
        return tengah
