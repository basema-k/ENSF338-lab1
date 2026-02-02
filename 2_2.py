def open_read_file():
    with open("pg2701.txt", "r", encoding="utf-8") as file:
        lines = file.read().splitlines()[40:] # create array, skip 40 lines
    
    return lines

def count_vowels():
    book_lines = open_read_file()
    counts = []
    
    for line in book_lines:
        words = line.lower().split()
        for word in words:
            count = 0
            for char in word:
                if char in "aeiouy":
                    count += 1
            counts.append(count)
                
    return counts

def average():
    vowels = count_vowels()
    count = 0
    words = 0
    for numbers in vowels:
        count += numbers
        words += 1

    average = count / words
    return average

def main():
    averageNumberOfVowels = average()
    print(averageNumberOfVowels)

main()

    

    

        
          



