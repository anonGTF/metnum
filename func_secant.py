from func import *


def secant(a, b, c, x0, x1, error):
    myfunc = MyFunc(a, b, c)
    err = 1
    x2 = None
    while err > error:
        y0 = myfunc.func(x0)
        y1 = myfunc.func(x1)
        x2 = x1 - y1 * ((x1 - x0) / (y1 - y0))
        y2 = myfunc.func(x2)
        err = abs(y2)
        # print(f'x0: {x0} x1: {x1} x2: {x2} y0: {y0} y1: {y1} y2: {y2} ')
        if err > error:
            x0 = x1
            x1 = x2

    return x2
