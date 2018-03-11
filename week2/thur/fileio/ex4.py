import json
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
with open('saved.json', 'r') as fh:
    saved = json.load(fh)
print(saved)
for i in saved:
    pyplot.plot(i)
#pyplot.plot(saved)
pyplot.savefig('plot.png')
pyplot.close()