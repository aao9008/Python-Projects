"""
while True:
    try:
        age = int(input('enter a number:'))
    except ValueError:
        print('invalid input')
        continue
    else:
        break
"""
x= 'The sky is blue'

def main(s):
    rdy_str = prepare_str(s)
    if palindrome(rdy_str) == True:
        print('String is palindrome')
    else:
        print('String is not palindrome')

def prepare_str(s):
    rdy_str = no_space(s)
    return rdy_str.lower()


def no_space(s):
    if " " not in s:
        return s
    else:
        for i in range(len(s)):
            if s[i] == ' ':
                return no_space(s[:i] + s[i + 1:])
# Line 31 slices out the space and returns the new str
# value to function no_space until all spaces are removed.

def reverse(s):
    reverse_str = ''
    for char in s:
        reverse_str = char + reverse_str
    return reverse_str

def palindrome(s):
    if s == reverse(s):
        return True
    else:
        return False

main(x)