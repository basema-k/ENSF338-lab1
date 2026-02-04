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

listlength = 1000

times = []
for _ in range(1000):
    numbers = [x for x in range(listlength)]
    random.shuffle(numbers)
    tm = timeit.timeit("findinlist(5, numbers)", 
                       setup="from __main__ import findinlist, numbers", 
                       number=100)
    times.append(tm/100)

avg = sum(times) / len(times)
print("Average time for list of length %d: %f" % (listlength, avg))

plt.figure()
plt.hist(times, bins=50, edgecolor='black', alpha=0.7)
plt.xlabel('Processing Time (s)')
plt.ylabel('Frequency')
plt.title('Distribution of Processing Times for Linear Search with 1000 trials')
plt.grid(True, alpha=0.3)

plt.savefig('output.3.3.png')
plt.show()

print(f"The average processing time is: {avg:.2e} seconds")