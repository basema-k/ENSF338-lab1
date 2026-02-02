import timeit

def pow2(n):
    return pow(2, n)

def pow2ThousandForLoop():
    powers = []
    for i in range(1000):
        power = pow2(i)
        powers.append(power)
    
    return powers

def pow2ThousandListComprehension():
    powers = [pow2(i) for i in range(1000)]
    return powers

def timePow2():
    def pow2TenThousand():
        return pow2(10000)

    timeElapsed = timeit.timeit(pow2TenThousand, number = 10000)
    print(f'Elapsed time: {timeElapsed:.6f} seconds.')

def timePow2Thousand():
    timeElapsedForLoop = timeit.timeit(pow2ThousandForLoop, number = 1000)
    timeElapsedListComprehension = timeit.timeit(pow2ThousandListComprehension, number = 1000)

    print(f'Elapsed time using the for loop: {timeElapsedForLoop:.6f} seconds.')
    print(f'Elapsed time using list comprehension: {timeElapsedListComprehension:.6f} seconds.')

def main():
    timePow2()
    timePow2Thousand()

main()
