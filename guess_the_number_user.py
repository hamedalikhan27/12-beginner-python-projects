## Computer will try to guess the secter number chosen by the User
## Computer will generate a number between a specified low and high range
## Computer will display the guess to user and collect feedback
## The user should respond with 
##      H if guess is too high
##      L if guess is too low
##      C if guess is correct
## based on the feedback computer will adjust the range accordingly and continue guessing until it finds the correct number

import random

low = 1
high = 10
feedback = ''

while feedback != 'c':

    if (high != low and low < high):
        guess_a_number = random.randint(low, high)
    else:
        guess_a_number = low

    feedback = input(f"Is {guess_a_number} too high (H), too low (L), or correct (C): ").lower()

    if (feedback == 'h'):
        high = guess_a_number - 1
    elif (feedback == 'l'):
        low = guess_a_number + 1

print(f"Yay! Computer guessed you secter number {guess_a_number}, correctly")
    
    

