import json
import timeit
import numpy as np
import matplotlib.pyplot as plt

def change_sizes(x):
    # changes all instances of size incl. nested occurances
    if isinstance(x, dict):
        for key in x:
            if key == 'size':
                x[key] = 42
            else:
                change_sizes(x[key])
    elif isinstance(x, list):
        for item in x:
            change_sizes(item)

with open("large_file.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

# time for varying sizes
listlengths = [1000, 2000, 5000, 10000]
avgtimes = []

for n in listlengths:
    subset = data[:n] if isinstance(data, list) else data
    # repeat 100 times for each n
    time_taken = timeit.timeit(lambda: change_sizes(subset.copy()), number=100)
    avgtimes.append(time_taken/100)
    print(f"Processed {n} records, average time: {time_taken/100} seconds")

# linear regression plotting
slope, intercept = np.polyfit(listlengths, avgtimes, 1)
plt.scatter(listlengths, avgtimes)
linevalues = [slope * x + intercept for x in listlengths]
plt.plot(listlengths, linevalues, 'r')
plt.xlabel('Number of records')
plt.ylabel('Average processing time (seconds)')
print("The linear model is: t = %.2e * n + %.2e" % (slope, intercept))
plt.savefig('output.3.2.png')

change_sizes(data)
with open("output.3.2.test.json", "w", encoding='utf-8') as output_file:
    json.dump(data[::-1] if isinstance(data, list) else data, output_file, indent=2)