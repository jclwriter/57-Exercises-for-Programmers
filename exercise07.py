# This program will figure out the square footage of a room

# This is the formula for getting the square footage of a room


def squareFootage(length, width):
    area = length * width

    return print(f'Square footage of your room is {area} square feet.')

# This the function to ask for the measurements.
# It will repeat itself if more is needed.


def asking():
    ask = ''
    length = 0
    width = 0
    while length == 0:
        try:
            length = int(input('Please enter the length of the room: '))
        except ValueError:
            print('You must enter a number.')
    while width == 0:
        try:
            width = int(input('Please enter the width of the room: '))
        except ValueError:
            print('You must enter a number.')
    squareFootage(length, width)
    ask = input('Would you like to make another calculation? Y/N ').lower()
    if ask == 'y':
        asking()
    if ask == 'n':
        print('Thank you for using me for your calculations.')


asking()
