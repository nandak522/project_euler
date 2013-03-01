'''
25
'''


def fabonacci():
    a ,b = 0,1
    cnt = 1
    while True:
        if len(str(b)) == 1000:
            return cnt
        cnt+=1
        a,b=b,a+b
        

if __name__ == '__main__':
    print "Term to print 1000 digits %s" %fabonacci()
