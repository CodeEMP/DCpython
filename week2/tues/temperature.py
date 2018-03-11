import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot

def ctof(x):
    return x * 1.8 + 32
graph = list(range(1, 101))
tempc = float(input("What's the temperature in Celcius? "))
tempf = ctof(tempc)

pyplot.plot(graph, graph, tempf)
pyplot.savefig('ex7.png')
pyplot.close()