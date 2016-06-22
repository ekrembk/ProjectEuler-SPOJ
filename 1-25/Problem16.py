#ProjectEuler problem 16
#Solved: 12 May 2016

def sumDigit(n):
    lst = list(str(n))
    lst = map(lambda x: int(x), lst)
    return sum(lst)

print sumDigit(2**1000)
