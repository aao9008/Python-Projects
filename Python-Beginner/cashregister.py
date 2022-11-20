print('Enter price of the first item:')
first_item= float(input())

print('Enter Price of the second item:')
second_item= float(input())

print('Does customer have a club card? (Y/N):')
club_card= input()

print('Enter tax rate, e.g. 5.5 for 5.5% tax:')
tax= float(input())

base_price= first_item + second_item
base_price= f'{base_price: .2f}'

if (first_item > second_item):
    second_item= second_item * 0.50
elif (first_item == second_item):
    first_item= first_item * 0.50
else:
    first_item= first_item * 0.50

item_total= first_item + second_item

if (club_card == 'Y' or club_card == 'y'):
    item_total= item_total * 0.90
elif (club_card == 'N' or club_card == 'n'):
    item_total= item_total * 1
grand_total= (item_total * (tax/100)) + item_total

grand_total= f'{grand_total: .2f}'
item_total= f'{item_total: .2f}'

print(type(item_total))

print('Base price =', base_price)
print('Price after discounts =', item_total)
print('Total price =', grand_total)