'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

from clock import Timer


BIG_NUMBER = 2000000


def is_prime(number):
    if number % 2 == 0:
        return False
    max_possible_factor = int(number ** 0.5)
    for i in range(3, max_possible_factor + 1, 2):
        if number % i == 0:
            return False
    return True


def summation_of_primes(big_number):
    sum_of_primes = 2
    lst = range(3, big_number, 2)
    for number in lst:
        if is_prime(number):
            # print 'prime:', number
            sum_of_primes += number
    return sum_of_primes

if __name__ == '__main__':
    with Timer() as t:
        print 'answer:', summation_of_primes(BIG_NUMBER)
    print 'Time taken:%.3f seconds' % t.interval
