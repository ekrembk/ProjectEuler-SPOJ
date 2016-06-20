#ProjectEuler problem 5
#Solved: 8 Feb 2016

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
            
def primeFac(x): #Prime factorization function
    if isPrime(x):
        return {x:1}
    
    factors = dict()
    counter = 1
    while True:
        if isPrime(counter): #check if counter is prime
            if x % counter == 0: #if x is divisible by prime
                while x % counter == 0: #do while still divisible
                    if counter in factors:
                        factors[counter] += 1
                    else:
                        factors[counter] = 1
                    x = x / counter
                        
        counter += 1
        if counter > x:
            return factors

def main():
    multip = dict()
    num = 20
    for i in range(1, num + 1):
        factors = primeFac(i)
        for j in factors:
            if j in multip:
                if multip[j] < factors[j]:
                    multip[j] = factors[j]
            else:
                multip[j] = factors[j]

    product = 1
    for k in multip:
        product *= k**multip[k]
    print product

if __name__ == '__main__':
    main()
