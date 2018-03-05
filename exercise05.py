'''
Exercise 5: Simple Math
This program will prompt for 2 numbers.
The sum, difference, product and quotient of this numbers will be printed.

num1 + num2 = num3
num1 - num2 = num3
num1 * num2 = num3
num1 / num2 = num3

'''
try:
    num1 = int(input('Please enter the first number: '))
except ValueError:
    num1 = int(input('You must enter an integer: '))
try:
    num2 = int(input('Please enter the second number: '))
except ValueError:
    num2 = int(input('You must enter an integer: '))

adding = num1 + num2
subtract = num1 - num2
multiply = num1 * num2
division = num1 // num2

print(f'{num1} + {num2} = {adding}')
print(f'{num1} - {num2} = {subtract}')
print(f'{num1} * {num2} = {multiply}')
print(f'{num1} / {num2} = {division}')
