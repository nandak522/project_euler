'''
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

from clock import Timer

MAX_INT = 1000

req = []

with Timer() as t:
    for i in range(3, MAX_INT):
        if (i % 3 == 0) or (i % 5 == 0):
            req.append(i)
print 'answer:', reduce(lambda x, y: x+y,  req)
print 'Time taken:%.3f seconds' % t.interval
