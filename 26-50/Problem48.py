#ProjectEuler problem 48
#Solved: 17 Jun 2016

total = 0

for i in range(1,1001):
    total += i**i

counter = 10
last_ten = ''
for i in range(10):
    index = len(str(total)) - counter
    last_ten += str(total)[index]
    counter -= 1

print last_ten
