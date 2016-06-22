#ProjectEuler problem 34
#Solved: 10 May 2016
#NOTE: This code is could be further optimized. I will work on it sometime (hopefully)

def factorial(x):
    if x == 1 or x == 0:
        return 1
    else:
        return x*factorial(x-1)

def main():    
    final_total = 0
    for i in range(3,10000000):
        digits = list(str(i))
        total = 0
        for n in digits:
            a = factorial (int(n))
            total += a
        if total == i:
            final_total += i
        if total > i and i > 1000000:
            return final_total

if __name__ == '__main__':
    print main()
