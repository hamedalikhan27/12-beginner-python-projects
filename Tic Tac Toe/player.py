import random

## Player Base Class
class Player:
    def __init__(self, letter):
        self.letter = letter
    
    def get_move(self, game):
        pass

## RandonComputerPlayer child Class, inhiriting Player Base Class
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

## HumanPlayer child Class, inhiriting Player Base Class
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        value = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            ## we'll check whether or not this is a valid input by casting
            ## it to an Integer, if it is not, then we say its invalid
            ## if that spot is not available on the board, we also say its invalid
            try:
                value = int(square)
                if value not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid Square, Try again")
            
            return value