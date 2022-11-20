print('Please enter the amount of money to convert:')
dollars= int((input('# of dollars:')))
cents= int(input('# of cents:'))

total_cents=(dollars*100)+cents

quarters= total_cents // 25
dimes= (total_cents % 25) // 10
nickels= ((total_cents % 25) % 10) // 5
pennies= (((total_cents % 25) % 10) % 5) // 1

print('The coins are', quarters, 'quarters,', dimes, 'dimes,', nickels, 'nickels and', pennies,
      'pennies')
