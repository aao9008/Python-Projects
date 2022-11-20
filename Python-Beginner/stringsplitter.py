import math
print('Enter an odd length string:')
string = input()

middle_index = math.floor(len(string)/2)
middle_char = string[middle_index]

first_half = string[:middle_index]
second_half = string[middle_index + 1:]

print('Middle character:',middle_char)
print('First half:', first_half)
print('Second half:',second_half)