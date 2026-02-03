import random
import timeit
from matplotlib import pyplot as plt
plt.rcParams['figure.figsize'] = [10, 5]
import numpy as np


def findinlist(n, l):
    for i in range(len(l)):
        if l[i] == n:
            return True
    return False

avgtimes = []

listlengths = [1000, 2000, 5000, 10000]
for listlength in listlengths:
    
    numbers = [x for x in range(listlength)]
    rez = []

    for i in range(1000):
        random.shuffle(numbers)
        tm = timeit.timeit("findinlist(5, numbers)", setup="from __main__ import findinlist, numbers", number=100)
        rez.append(tm/100)

    avg = sum(rez) / len(rez)
    avgtimes.append(avg)
    print("Average time for list of length %d: %f" % (listlength, avg))

slope, intercept = np.polyfit(listlengths, avgtimes, 1)
plt.scatter(listlengths, avgtimes)
linevalues = [slope * x + intercept for x in listlengths]
plt.plot(listlengths, linevalues, 'r')
plt.xlabel('# of records')
plt.ylabel('Avg. Processing Time (s)')
plt.title('Input Size Vs. Runtime for Linear Search')
plt.savefig('output.3.2.png')

print("The linear model is: t = %.2e * n + %.2e" % (slope, intercept))