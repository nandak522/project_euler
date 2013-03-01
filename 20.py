'''

'''

def factorial(number):
    fact = 1
    while(number>1):
        fact = fact *number
        number-=1
    return fact 

def sum_of_number(num):
    sum =0
    for i in str(num):
        sum+=int(i)
    return sum

if __name__ == '__main__':
    NUM=100
    print "Sum of the digits in number 100=%s" %sum_of_number(factorial(NUM))
