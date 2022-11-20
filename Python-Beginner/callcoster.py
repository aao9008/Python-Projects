print('Enter the day the call started at:')
day= input()

print('Enter the time the call started at (hhmm):')
time= input()

print('Enter the duration of the call (in minutes):')
duration= float(input())

day_list= ['Mon','Tue','Wed','Thr','Fri']
weekend_list= ['Sat','Sun']

if day in day_list and '0800' <= time <= '1900':
    cost= duration * 0.40
elif day in day_list and time < '0800' or time > '1900':
    cost= duration * 0.25
elif day in weekend_list:
    cost= duration * 0.15

print(f'This call will cost ${cost:0.2f}')
