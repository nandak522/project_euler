'''
power(2, 15) = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number power(2, 1000)?
'''

print reduce(lambda x,y:int(x)+int(y), list(str(pow(2, 1000))))