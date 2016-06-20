#ProjectEuler problem 4
#Solved: 7 Feb 2016

def check_palindromic(num):
    lst = list(str(num))
    if lst[:len(lst)/2] == lst[:len(lst)/2 - 1:-1]:
        return True
    else:
        return False

def main():
    i = 899
    a = 0
    max_num = 0
    numbers = range(100,1000)
    while(i >= 100):
        x = numbers[a]
        y = numbers[i]
        if check_palindromic(x*y) and x*y > max_num:
            max_num = x*y
        if (a == 899):
            i -= 1
            a = 0
        a += 1
    print max_num

if __name__ == '__main__':
    main()
