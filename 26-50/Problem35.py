#ProjectEuler problem 35
#Solved: 10 May 2016

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

def circulate(x):
    numbers = []
    new_number = list(str(x))
    while True:
        new_number.append(new_number[0])
        new_number.pop(0)
        if ''.join(new_number) not in numbers:
            numbers.append(int(''.join(new_number)))
        else:
            return numbers
def main():
    counter = 0
    for i in range(10**6):
        if not isPrime(i):
            continue
        numbers = circulate(i)
        for i in numbers:
            if not isPrime(i):
                break
        else:
            counter += 1
    return counter

if __name__ == '__main__':
    print main()
