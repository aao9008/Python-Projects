print('Enter a character:')
char = input()

if char.islower() == True:
    print(char,"is a lower case letter.")
elif char.isupper() == True:
    print(char,'is an upper case letter.')
elif char.isdigit() == True:
    print(char,'is a digit.')
elif char.isalnum() == False:
    print(char,'is a non-alphanumeric character.')