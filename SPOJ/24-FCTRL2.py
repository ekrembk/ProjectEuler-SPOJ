def fac(n):
    if n == 1:
        return 1
    else:
        return n*fac(n-1)
 
t = input()
for i in range(t):
    print fac(input())
