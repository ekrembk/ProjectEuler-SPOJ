#ProjectEuler problem 12
#Solved: 16 Jun 2016

import math

def isPrime(x):
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

def primeFac(x):
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

def main(n):
    num = n*(n+1)/2

    f1 = primeFac(n)
    f2 = primeFac(n + 1)
    z = dict()

    for i in f1:
        if i in f2:
            z[i] = f2[i] + f1[i]
        else:
            z[i] = f1[i]

    for j in f2:
        if j not in z:
            z[j] = f2[j]

    if 2 in z:
        if z[2] == 1:
            del z[2]
        else:
            z[2] -= 1

    factors = 1
    for k in z:
        factors *= (z[k] + 1)

    return factors


a = 1
f = 1
while f <= 500:
    f = main(a)
    a += 1

print (a-1)*a/2
