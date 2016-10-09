def Z(n):
    if n >= 5:
        remainder = n / 5
        return remainder + Z(remainder)
    else:
        return 0
 
T = input()
numbers = []
for i in range(T):
    numbers.append(input())
for n in numbers:
    print Z(n)
