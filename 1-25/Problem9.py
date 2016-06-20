#ProjectEuler problem 9
#Solved: 23 Apr 2016

import random

def main():
    while True:
        a = random.randrange(0,333)
        b = random.randrange(0,500)
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            return a*b*c

if __name__ == '__main__':
    print main()
