# Program to enter a list of numbers and find an average
# Author: Tom Weldon

# Assigning numbers to list
numbers = []

# Request an input number
number = int(input('Please enter a number (enter 0 to quit): '))

# While loop to append input number to numbers list
# while input is not equal to 0
while number != 0:
    numbers.append(number)
    number = int(input('Please enter another number (enter 0 to quit): '))

# Print the input numbers
for value in numbers:
    print(value, end=' ')

# Calculate average of numbers list
average = float(sum(numbers) / len(numbers))

# Print average of numbers list
print(' ')
print('The average of entered numbers is {:.2f}'.format(average) )
