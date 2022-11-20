print('Please enter the number of coins:')
a=int(input('# of quarters:'))
b=int(input('# of dimes:'))
c=int(input('# of nickels:'))
d=int(input('# of pennies:'))

quarters= a*25
dimes= b*10
nickels= c*5
pennies= d*1

total_money= quarters+dimes+nickels+pennies

total_dollars= total_money//100
total_cents= total_money%100

print("The total is", total_dollars,"dollars and",total_cents,"cents")