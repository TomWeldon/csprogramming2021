# Write a program that prompts the user to input 
# a number until the correct numvber is inputted
# Author: Tom Weldon G00398828

numberToGuess = 30
guess = int(input('Please enter a number: '))

while guess != numberToGuess:
    print('Wrong')
    if guess < numberToGuess:
        print('Your number {} was too low'.format(guess))
        guess = int(input('Please guess again: '))
    else: 
        print('Your number {} was too high'.format(guess))    
        guess = int(input('Please guess again: '))
print('Well done! yes the number was {}'.format(numberToGuess))
