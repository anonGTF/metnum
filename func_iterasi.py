from func import *


def iterasi(a, b, c, tebakan, error):
    myfunc = MyFunc(a, b, c)
    err = 1

    while abs(err) > error:
        yx = myfunc.func_gx(tebakan)
        err = tebakan - yx
        # print(f'tebakan: {tebakan} yx: {yx} err: {err}')
        if abs(err) > error:
            tebakan = yx

    return tebakan
