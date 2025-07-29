## hangman
## computer will pick a word from the list of words
## loop over this part until user guess the complete word
    ## request user to enter a letter
    ## if entered letter is in the chosen word, then remove it from chosen word
    ## else: let user know, the letter is not in the chosen word
    ## show the list/set of used letters
## once the chosen word is completed, display the word

import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def display_remaining_letters(valid_word):
    word_blank = []
    for letter in valid_word:
        if(letter in used_letters):
            word_blank.append(letter)
        else:
            word_blank.append("-")
    print("".join(word_blank))

valid_word = get_valid_word(words)
word_letters = set(valid_word)
used_letters = set()
alphabets = set(string.ascii_uppercase)
lives = 7

while len(word_letters) > 0 and lives > 0:

    print(f"You have {lives} lives left & Used Letters: " + ''.join(used_letters))
    display_remaining_letters(valid_word)

    user_letter = input("Enter a letter: ").upper()
    if (user_letter in alphabets - used_letters):
        used_letters.add(user_letter)
        if(user_letter in word_letters):
            word_letters.remove(user_letter)
        else:
            lives = lives - 1
            print(f"{user_letter} is not in the Word")
    elif(user_letter in used_letters):
        print(f"You have already used {user_letter}")
    else: 
        print("Please enter a valid letter.")

if(lives == 0):
    print(f"No lives left. You Lost. The word was {valid_word} Try again")
else:
    print(f"Yah!, you have guess the word {valid_word}")
