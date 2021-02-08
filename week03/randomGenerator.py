#program that prints out a random number between 1 and 10
#Author: Tom Weldon G00398828

import random

x = int(input('Please enter first number: '))
y = int(input('Please enter second number: '))

number = random.randint(x,y)

print('Here is a random number {} '.format(number))