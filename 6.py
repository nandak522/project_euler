'''
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
'''

from clock import Timer

MAX_INT = 100


def compute_sum_numbers(n):
    return n*(n+1)/2


def compute_sum_of_squares(n):
    return n*(n+1)*(2*n+1)/6

with Timer() as t:
    print 'answer:', compute_sum_of_squares(MAX_INT) - (compute_sum_numbers(MAX_INT) ** 2)
print 'Time taken:%.3f seconds' % t.interval
