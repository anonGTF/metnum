from func import *


def newton_raphson(a, b, c, tebakan, error):
    myfunc = MyFunc(a, b, c)
    err = 1

    while err > error:
        x1 = myfunc.nilaix1(tebakan)
        err = tebakan - x1
        # print(f"x: {tebakan} fx: {myfunc.func(tebakan)} f'x: {myfunc.func_der(tebakan)} x1: {x1} err: {err}")
        if err > error:
            tebakan = x1

    return tebakan
