'''
This program allows user input, then counts the string,
the user can not enter nothing.
'''

user = input('Enter a string: ')
while user == '':
    user = input('Input can not be blank, please try again. ')

string_length = len(user)
print(f'{user} has {string_length} characters')
