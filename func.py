import matplotlib.pyplot as plt
import numpy as np
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

    def grafik_kuadrat(self):
        # 100 linearly spaced numbers
        x = np.linspace(-5, 5, 100)

        # the function, which is y = x^2 here
        y = self.a * x ** 2 + self.b * x + self.c

        # setting the axes at the centre
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')

        # plot the function
        plt.plot(x, y, 'r')

        # show the plot
        plt.show()