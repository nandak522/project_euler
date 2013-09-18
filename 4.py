'''
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

from clock import Timer


def is_palindrome(number):
    return str(number) == str(number)[::-1]


def main():
    small_int = 100
    big_int = 999
    highest_product = 0
    for first_number in range(big_int, small_int-1, -1):
        for second_number in range(first_number, small_int-1, -1):
            product = first_number * second_number
            if is_palindrome(product) and product > highest_product:
                highest_product = product
    return highest_product

if __name__ == '__main__':
    with Timer() as t:
        print 'answer:', main()
    print 'Time taken:%.3f seconds' % t.interval
