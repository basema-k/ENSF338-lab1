import sys
import math
def do_stuff():
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])

    d = b**2 - 4*a*c
    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        print(f'The solutions are: {root1}, {root2}') # fixed quotation mark
    elif d == 0:
        root = -b / (2*a)
        print(f'The solution is: {root}') # fixed quotation mark
    else:
        print('There are no real solutions.')
do_stuff()

'''
Part 2.1 - Find the Error
i) The code shown is meant to find the roots of a quadratic equation 
    using the quadratic formula (or says if there aren't any). 
    It takes in values for a, b, and c as the coefficients of the 3 terms.
ii) The error is contained within the print statements, 
    where the opening and closing quotation marks are not the same.


'''
