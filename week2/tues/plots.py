import math
import matplotlib
from numpy import arange
matplotlib.use("Agg")

from matplotlib import pyplot

ex2_output = []

def ex2(x):
    return x + 1

ex2_list = list(range(-3, 4))
for x in ex2_list:
    ex2_output.append(ex2(x))

ex3_output = []

def ex3(x):
    return x * x

ex3_list = list(range(-100, 101))
for x in ex3_list:
    ex3_output.append(ex3(x))

ex4_output = []

def ex4(x):
    if x % 2 == 0:
        return 1
    else:
        return -1

ex4_list = list(range(-5, 6))
for x in ex4_list:
    ex4_output.append(ex4(x))

ex5_output = []

def ex5(x):
    it = math.sin(x)
    return it

ex5_list = list(arange(-5, 6, 0.1))
for x in ex5_list:
    ex5_output.append(ex5(x))


pyplot.plot(ex2_list, ex2_output)
pyplot.savefig('ex2.png')
pyplot.close()
pyplot.plot(ex3_list, ex3_output)
pyplot.savefig('ex3.png')
pyplot.close()
pyplot.bar(ex4_list, ex4_output)
pyplot.savefig('ex4.png')
pyplot.close()
pyplot.plot(ex5_list, ex5_output)
pyplot.savefig('ex5.png')
pyplot.close()