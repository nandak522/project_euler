'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10001st prime number?
'''

from clock import Timer

POINTER = 10001

def is_prime(number):
    max_possible_factor = int(number ** 0.5)
    for i in range(2, max_possible_factor + 1):
        if number % i == 0:
            return False
    return True


def main():
    counter = 0
    number = 2
    while True:
        if is_prime(number):
            counter += 1
            if counter == POINTER:
                return number
        number += 1


if __name__ == '__main__':
    with Timer() as t:
        print 'answer:', main()
    print 'Time taken:%.3f seconds' % t.interval
