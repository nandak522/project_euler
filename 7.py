'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10001st prime number?
'''

from clock import Timer


def main():
    pass


if __name__ == '__main__':
    with Timer() as t:
        print 'answer:', main()
    print 'Time taken:%.3f seconds' % t.interval