number = int(input('Please enter an integer: '))

while number > -1 or number < -1:
    number = int(input('Please enter an integer: '))
if (number % 2) == 0:
    print('The number {} is even'.format(number))
else:
    print('The number {} is odd'.format(number))