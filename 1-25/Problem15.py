#ProjectEuler problem 15
#Solved: 12 May 2016

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)

print factorial(40)/(factorial(20))**2
