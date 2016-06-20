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
