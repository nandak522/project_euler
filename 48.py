'''
'''


def last_ten_digits(number):
    sum = 0
    for i in range(1,number):
        sum += pow(i,i)
    print sum
    return str(sum)[-10:]


if __name__ == '__main__':
    print "sum %s" %last_ten_digits(1000)

