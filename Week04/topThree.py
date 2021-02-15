import random
# Program to print top 3 numbers of 10 random numbers
# between 0 and 100
# Author: Andrew Beatty


howMany = 10 # The number of random numbers
topHowMany = 3 # The top 3 numbers
rangeFrom = 0 # range from
rangeTo = 100 # range to

# List of numbers
numbers = []

# Select 10 random numbers in a for loop and append to list
# Print the number of random numbers and thge actual numbers
for i in range(0,10):
    numbers.append(random.randint(rangeFrom,rangeTo))
print('{} random numbers\t {}'.format(howMany, numbers))

# Make a copy of numbers list
# Sort the list in reverse
# Print the top three numbers in the numbers list(topOnes)
# and print the list range from 0 to 3 not including 3
topOnes = numbers.copy()
topOnes.sort(reverse = True)
print('The top {} are \t\t {}'.format(topHowMany, topOnes[0:topHowMany]))