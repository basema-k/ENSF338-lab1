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

# time first 1000 records 1000 times
subset = data[:1000] if isinstance(data, list) else data
times = timeit.repeat(lambda: change_sizes(subset.copy()), number=1, repeat=1000)

# make histogram
plt.hist(times, bins=30)
plt.xlabel('Processing time (seconds)')
plt.ylabel('Frequency')
plt.savefig('output.3.3.png')
plt.close()

change_sizes(data)
with open("output.3.3.test.json", "w", encoding='utf-8') as output_file:
    json.dump(data[::-1] if isinstance(data, list) else data, output_file, indent=2)