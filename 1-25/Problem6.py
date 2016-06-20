#ProjectEuler problem 6
#Solved: 8 Feb 2016

def main():
    num = 101
    
    para_sqr = sum(range(num))**2
    
    sqr = 0
    for i in range(num):
        sqr += i**2

    print para_sqr - sqr

if __name__ == '__main__':
    main()
