#*
# Computer will generate a number from a certain range i.e. 1 to 10

# This part has to be repeated as long as user didn't guess the correct number
    # computer will ask user to enter (guess) a number between 1 to 10
    # if the guessed number is greater then generated number, print ("Too High")
    # if the guessed number is less then generated number, print ("Too Low")

# if the guessed number is same as generated number, print ("Congrats")
# *#

import random

computer_generated_number = random.randint(1, 10)
user_input = 0

while user_input != computer_generated_number:
    user_input = int(input("Enter a number between 1 to 10: "))
    if(user_input >= 1 and user_input <= 10):
        if(user_input > computer_generated_number):
            print("Sorry, guess again, Too High")
        elif(user_input < computer_generated_number):
            print("Sorry, guess again, Too Low")
    else:
        print("Out of range")
print(f"Yay, You have guess the number correctly. {computer_generated_number}")