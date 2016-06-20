#ProjectEuler problem 14
#Solved: 11 May 2016

def operation(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3*n + 1
        

def collatz(n):
    count = 1
    while True:
        count += 1
        n = operation(n)
        if n == 1:
            return count

max_count = 0    
for i in range(1,10**6):
    if collatz(i) > max_count:
        maximum = i
        max_count = collatz(i)

print maximum
