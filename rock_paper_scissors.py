## Ask user to pick one from following options [Rock / Paper / Scissors]
## Computer will pick a random option from the given choice [Rock / Paper / Scissors]
## apply few conditions to determine the winner

import random

user = input("Pick: 'R' for Rock, 'P' for Paper, 'S' for Scissors: ").lower()
computer = random.choice(['r','p','s'])

## r > s, s > p, p > r
print(f"You: {user} | Computer: {computer}")
if((user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r')):
    print("You Won!")
elif(user == computer):
    print("It is a tie")
else:
    print("You lost!")