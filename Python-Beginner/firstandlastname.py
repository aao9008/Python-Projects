print('Please enter first and last name separated by a space:')
fullname = input()

space_index = fullname.find(' ')
first_name = fullname[:space_index]
last_name = fullname[space_index+1:]
initials = first_name[0] + last_name[0]

print('first name:',first_name)
print('last name:',last_name)
print('initials:',initials)