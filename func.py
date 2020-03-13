import math


class MyFunc:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def func(self, x):
        return self.a*x**2 + self.b*x + self.c

    def nilaix(self, ba, bb):
        return (self.func(bb)*ba - self.func(ba)*bb)/(self.func(bb) - self.func(ba))

    def func_gx(self, x):
        return math.sqrt((-1 * (self.b*x + self.c)) / self.a)

    def func_der(self, x):
        return self.a*2*x + self.b

    def nilaix1(self, x):
        return x - self.func(x)/self.func_der(x)