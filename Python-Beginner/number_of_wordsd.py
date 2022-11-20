print('Please enter a line of text.')
line = input()
space_count = 0
x= len(line) - 1

for index in line:
    if index == " " :
        space_count = space_count + 1
word_count = space_count + 1

print(word_count)