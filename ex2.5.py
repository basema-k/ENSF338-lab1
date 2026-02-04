import json
import timeit

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

# avg of 10 runs
time_taken = timeit.timeit(lambda: change_sizes(x), number=10)

print(f"Average time: {time_taken/10} seconds")

with open("output.2.5.test.json", "w", encoding='utf-8') as output_file:
    json.dump(x[::-1], output_file, indent=2)


