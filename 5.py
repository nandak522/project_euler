'''
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
'''

MIN = 20
divisibles = range(1,MIN+1)
is_divisible = False
while True:
    for div in divisibles:
        if MIN%div == 0:
            is_divisible = True
        else:
            is_divisible = False
            MIN += 1
            break
    if is_divisible:
        print 'Number:%s' % MIN
        break