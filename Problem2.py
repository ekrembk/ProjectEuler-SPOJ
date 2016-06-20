#ProjectEuler problem 2
#Solved: 5 Feb 2016

def fib():
    fibonacci_list = [1,2]
    total = 0
    index_count = 0
    while(total <= 4*10**6):
        total = fibonacci_list[index_count] + fibonacci_list[index_count + 1]
        fibonacci_list.append(total)
        index_count += 1
    return fibonacci_list

final_sum = 0
for item in fib():
    if item % 2 == 0:
        final_sum += item
print final_sum
