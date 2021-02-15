# Write a program that prompts the user to input 
# a number until the correct numvber is inputted
# Author: Tom Weldon G00398828

# Number to guess
numberToGuess = 30
# Request to input a number
guess = int(input('Please enter a number: '))

# While loop when guess is not equal to numberToGuess
# if statement for advising guess is too low or too high
while guess != numberToGuess:
    print('Wrong')
    if guess < numberToGuess:
        print('Your number {} was too low'.format(guess))
        guess = int(input('Please guess again: '))
    else: 
        print('Your number {} was too high'.format(guess))    
        guess = int(input('Please guess again: '))

# Out put to screen if guess is equal to numberToGuess
print('Well done! yes the number was {}'.format(numberToGuess))
