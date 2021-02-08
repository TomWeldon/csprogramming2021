#This program reads in string and strips
#any leading or trailing spaces it also changes to lowercase
#Author: Tom Weldon G00398828

rawString = input('Please enter a string: ')
normalisedString = rawString.strip().lower()

lengthOfRawString = len(rawString)
lengthOfNormalised = len(normalisedString)

print('The string normailised is {}'.format(normalisedString))
print('We reduced the input string from {} to {}'.format(lengthOfRawString, lengthOfNormalised))