#ProjectEuler problem 17
#Solved: 15 Jun 2016

def numbers(x):
    
    single_digits = ['one','two','three','four','five','six','seven','eight','nine']
    tens = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    double_digits = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    
    if 0 < x < 10: #e.g. 7
        return single_digits[x - 1] # seven

    elif 9 < x < 20: #e.g. 13
        return tens[x - 10] #thirteen

    elif 19 < x < 100: #e.g. 45
        output = ''
        output += double_digits[x/10 - 2] #45/10 = 4 - 2 = 2 ==> fourty
        if x % 10 != 0:
            output += numbers(int(str(x)[1])) #five
        return output #fortyfive

    elif 99 < x < 1000: #e.g. 137
        output = ''
        output += numbers(int(str(x)[0])) #one
        output += 'hundred' #onehundred
        if x % 100 != 0:
            output += 'and' #onehundredand
            output += numbers(int(str(x)[1:])) #onehundredandthirtyseven
        return output

    elif x == 1000:
        return 'onethousand'

def main():
    counter = 0      
    for i in range(1,1001):
        counter += len(numbers(i))

    print counter

if __name__ == '__main__':
    main()
