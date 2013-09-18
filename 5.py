'''
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
'''

# NOTE: To make a number divisible by 1 till 20, which means lcm of 1 till 20
# is that number

from clock import Timer

MIN = 20


def gcd(a, b):
    '''
    Euclid's algorithm
    '''
    if b:
        return gcd(b, (a % b))
    return a


def lcm(a, b):
    return (a * b) / gcd(a, b)


with Timer() as t:
    small_positive_number = 1
    for number in range(1, 21):
        small_positive_number = lcm(small_positive_number, number)

    print 'answer:', small_positive_number

print 'Time taken:%.3f seconds' % t.interval
