from func import *


def newton_raphson(a, b, c, tebakan, error):
    myfunc = MyFunc(a, b, c)
    err = 1

    while err > error:
        x1 = myfunc.nilaix1(tebakan)
        err = tebakan - x1
        print("x: %6.4f f(x): %6.4f f'(x): %6.4f x1: %6.4f error: %6.4f " % (tebakan, myfunc.func(tebakan), myfunc.func_der(tebakan), x1, err))
        if err > error:
            tebakan = x1

    return tebakan
