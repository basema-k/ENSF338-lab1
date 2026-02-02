import json
import timeit
import matplotlib.pyplot as plt
import numpy as np

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
    x = json.load(f)

# iterate for diff. amount of records processed
records = [1000, 2000, 5000, 10000]
avgtimes = []

for n in records:
    # get first n records
    test_data = x[:n]
    # avg time of 100 runs
    tm = timeit.timeit("change_sizes(test_data)", 
                      setup="from __main__ import change_sizes, test_data", 
                      number=100)
    avg = tm / 100
    avgtimes.append(avg)
    print(f"Average time for {n} records: {avg}")

# plot results
slope, intercept = np.polyfit(records, avgtimes, 1)
plt.scatter(records, avgtimes)
plt.plot(records, [slope * r + intercept for r in records], 'r')
plt.savefig('output.3.2.png')

change_sizes(x)
with open("output.2.3.test.json", "w", encoding='utf-8') as output_file:
    json.dump(x[::-1], output_file, indent=2)


