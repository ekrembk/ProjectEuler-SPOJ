#ProjectEuler problem 7
#Solved: 9 Feb 2016

def isPrime(x): #Classic isPrime function <trial division>
    import math
    if x < 3:
        if x == 2:
            return True
        else:
            return False
    else:
        if x % 2 == 0:
            return False
        else:
            for i in range(3, int(math.sqrt(x)) + 1 , 2):
                if x % i == 0:
                    return False
            else:
                return True

def main():
    counter = 0
    i = 1
    while counter <= 10000:
        i += 1
        if isPrime(i):
            counter += 1
    print i

if __name__ == '__main__':
    main()
