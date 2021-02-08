#Program that read in two numbers
#and outputs the integer answer and remainder
#Author: Tom Weldon G00398828

x = int(input('Please enter first number: '))
y = int(input('Please enter the number you wat to divide by: '))

answer = int(x/y)
remainder = x%y

print('{} divide by {} is {} with remainder {}'.format(x, y, answer, remainder))