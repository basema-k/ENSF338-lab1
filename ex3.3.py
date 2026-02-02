import json
import timeit
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
    x = json.load(f)

# first 1000 records
test_data = x[:1000]

# avg time of 1000 runs
times = timeit.repeat("change_sizes(test_data)", 
                     setup="from __main__ import change_sizes, test_data", 
                     number=1,
                     repeat=1000)
print(f"Average time for 1000 records: {sum(times)/1000}")

# make histogram
plt.hist(times, bins=30, edgecolor='black')
plt.title('Time Distribution for 1000 Records (1000 runs)')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.savefig('output.3.3.png')

change_sizes(x)
with open("output.2.3.test.json", "w", encoding='utf-8') as output_file:
    json.dump(x[::-1], output_file, indent=2)