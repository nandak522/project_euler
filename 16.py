'''
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?


'''


def sum_of_digit(number):
    sum = 0 
    for num in number:
        sum += int(num)
    return sum

if __name__ == '__main__':
    NUM = pow(2,1000)
    print sum_of_digit(str(NUM))
