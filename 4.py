'''
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''


def is_palindrome(number):
    string = str(number)
    total_length = len(string)
    for index in range(total_length/2):
        if string[index] != string[total_length-index-1]:
            return False
    return True

def main():
    all_palindromes = []
    small_int = 111
    big_int = 999
    upper_bound = big_int
    while big_int > small_int:
        for i in range(big_int, small_int-1, -1):
            product = big_int*i
            if is_palindrome(product):
                all_palindromes.append(product)
        big_int -= 1
    return max(all_palindromes)

if __name__ == '__main__':
    print main()