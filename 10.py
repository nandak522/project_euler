'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

BIG_NUMBER = 2000000

def summation_of_primes(big_number):
    '''
    Following seive_of_eratosthenes, retrieve primes quickly:
    Lets say big_number is 20
    initial list :
    [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

    after filtering 2 multiples:
    [2, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    after filtering 3 multiples:
    [2, 3, 5, 7, 11, 13, 17, 19]

    after filtering 5 multiples:
    [2, 3, 5, 7, 11, 13, 17, 19]
    '''
    sum_of_primes = 0
    lst = range(2, big_number)
    print 'initial list size:%s' % len(lst)
    n = 0
    popper = lst.pop
    while n < len(lst):
        scanner = lst[n]
        print 'scanner:%s' % scanner
        index = n+1
        while index < len(lst):
            if lst[index] % scanner == 0:
                popper(index)
            index += 1
        print 'list size now:%s' % len(lst)
        sum_of_primes += scanner
        n += 1
    return sum_of_primes

if __name__ == '__main__':
    print summation_of_primes(BIG_NUMBER)