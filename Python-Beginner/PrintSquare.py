# square
print('enter posititve integer:')
n=int(input())

for i in range(n):
    print(n*'*')

# left aligned triangle
print('enter number:')
x=int(input())

for i in range(1,x+1):
    print(i*'*')

# right aligned triangle
print('enter number:')
y=int(input())

for i in range (1,y+1):
    line= (n-i)*" "+ i * '*'
    print(line)