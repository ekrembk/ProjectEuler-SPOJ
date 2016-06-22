#ProjectEuler problem 21
#Solved: 16 Jun 2016

def d(n):
    total = 0
    for i in range(1,n/2 + 1):
        if n % i == 0:
            total += i
    return total


def main():
    a = 1
    b = 0
    total = 0
    amicables = list()

    while a < 10000:
        b = d(a)
        
        if b > 10000 or b == a:
            a += 1
            continue
        
        if d(b) == a:
            if a not in amicables:
                amicables.append(a)
                amicables.append(b)
        a += 1
    print 'total: ',sum(amicables)
            
if __name__ == '__main__':
    main()
