#ProjectEuler problem 2
#Solved: 5 Feb 2016

def fib(n): #Returns the nth fibonacci number
    num1 = 1
    num2 = 1
    if n == 1 or n == 2:
        return 1
    elif n <1:
        raise ValueError('There is no %dth fibonacci number!' %n)
    elif type(n) != int:
        raise ValueError('Fibonacci requires an int input!')
    n -= 2
    for i in range(n):
        num3 = num1 + num2
        num1 = num2
        num2 = num3
    return num3

def main():
    total = 0
    n = 1
    a = 1
    while a < 4*10**6:
        if a % 2 == 0:
            total += a
