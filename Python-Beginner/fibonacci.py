print('Please enter a positive integer greater than 1:')
n = int(input())
previous_num = 0
next_num = 1

for i in range(n):
    if i == 1:
        result = i
    else:
        result = previous_num + next_num
        previous_num = next_num
        next_num = result
    print(result)











