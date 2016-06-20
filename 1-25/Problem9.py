#ProjectEuler problem 8
#Solved: 23 Apr 2016

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

p = 3 #start from prime number 3 and add 2 to the final sum later
      #to set a constat step size, 2.
total = 0
while p < 2*(10**6):
    if isPrime(p):
        total += p
    p += 2
print total + 2
