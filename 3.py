'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

from clock import Timer


MAX_INT = 600851475143


initial_divisor = 2
dividend = MAX_INT


with Timer() as t:
    while dividend > initial_divisor:
        if dividend % initial_divisor == 0:
            dividend = dividend / initial_divisor
            continue
        else:
            initial_divisor += 1
print 'answer:', initial_divisor
print 'Time taken:%.3f seconds' % t.interval
