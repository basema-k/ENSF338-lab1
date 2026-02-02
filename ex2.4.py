import timeit

def openReadFile():
    with open("pg2701.txt", "r", encoding="utf-8") as file:
        lines = file.read().splitlines()[40:] # create array, skip 40 lines
    
    return lines

def countVowels(bookLines):
    counts = []
    
    for line in bookLines:
        words = line.lower().split()
        for word in words:
            count = 0
            for char in word:
                if char in "aeiouy":
                    count += 1
            counts.append(count)
                
    return counts

def average(bookLines):
    vowels = countVowels(bookLines)
    count = 0
    words = 0
    for numbers in vowels:
        count += numbers
        words += 1

    average = count / words
    return average


def main():
    bookLines = openReadFile()

    def timedAverage():
        return average(bookLines)
    
    timeElapsed = timeit.timeit(timedAverage, number = 100)
    finalTime = timeElapsed / 100
    print(f'Execution time: {finalTime:.6f} seconds')

main()
