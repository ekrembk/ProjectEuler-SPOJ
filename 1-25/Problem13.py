#ProjectEuler problem 13
#Solved: 11 May 2016
#NOTE: For this code to work, a text file named '13.txt' containing 50 numbers provided in the problem is required in the same directory as this py file

def getNumber():
    fo = open('13.txt','r')
    numbers = []
    for i in range(100):
        numbers.append(int(fo.readline()))
    return numbers

number = sum(getNumber())

result = ''
for i in range(10):
    result += str(number)[i]
print result
