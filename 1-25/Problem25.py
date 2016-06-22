#ProjectEuler problem 25
#Solved: 23 Apr 2016

lst = [1,1,1]
i = 2
while (len(str(lst[2])) < 1000): 
    lst[2] = lst[0] + lst[1]
    lst[0] = lst[1]
    lst[1] = lst[2]
    i += 1
print i
