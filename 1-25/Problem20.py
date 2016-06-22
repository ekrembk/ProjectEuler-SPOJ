#ProjectEuler problem 20
#Solved: 15 Jun 2016

def fac(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*fac(n-1)

a = fac(100)
total = 0
for i in str(a):
    total += int(i)
print total
