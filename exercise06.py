'''
Exercise 6: Retirement Calculator
This program determines how many years you have left until retirement.
It will also catch if the user already should have retired, or is retiring now.
'''
import datetime

now = datetime.datetime.now()

current_age = int(input('What is your current age? '))
print('')
retire_age = int(input('What age would you like to retire? '))
print('')
time_left = retire_age - current_age
retire_year = now.year + time_left

if time_left > 0:
    print(f'It\'s {now.year}, so that means you can retire in {retire_year}.')

elif time_left == 0:
    print(f'You will retire this year, {now.year}')

else:
    print(f'You should have retired in, {retire_year}')
