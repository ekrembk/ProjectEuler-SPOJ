#ProjectEuler problem 30
#Solved: 20 Jun 2016

def fifth(n):
    total = 0
    for c in str(n):
        total += int(c)**5
    if n == total:
        return True

def main():
    total = 0
    #min decimal with 7 digits is greater than fifth power digits of 9999999
    #that is why the following loop holds true
    for i in range(2,10**6):
        if fifth(i):
            print 'number: ', i
            total += i
    print total

if __name__ == '__main__':
    main()
