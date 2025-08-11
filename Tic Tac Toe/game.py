import time
from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| '+' | '.join(row)+' |')

    @staticmethod
    def print_board_nums():
        board_numbers = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in board_numbers:
            print('| '+' | '.join(row)+' |')
    
    def available_moves(self):
        return [i for (i, spot) in enumerate(self.board) if spot == " "] ## compressing below mention code in one line
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     if spot == " ":
        #         moves.append(i)
        # print(moves)
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        # if valid move, then make a move (assign square to letter)
        # then return True, if Invalid move, then return False
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # winner if 3 in row anywhere... we have to check all of these
        #lets start with row
        row_index = square // 3
        row = self.board[row_index * 3 : (row_index+1) * 3]
        if all([spot == letter for spot in row]):
            return True 
        
        # columns check
        col_index = square % 3
        column = [self.board[col_index+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # check diagonals
        # but only if the square is an even number (0,2,4,6,8)
        # these are only move possible to win a diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True
            
        # if all of these fails
        return False

def play(game, x_player, o_player, print_board=True):
    # this function returns the winner of the game (i.e. letter), or None for a tie
    if print_board:
        game.print_board_nums()

        letter = 'X' ## starting letter
        # Iterate while the game still has empty squares
        # we don't have to worry about the winner yet, we'll just return the winner
        # which will just break the loop
        while game.empty_squares():
            # get the move from appropriate user
            if letter == 'O':
                square = o_player.get_move(game)
            else:
                square = x_player.get_move(game)
        
            if game.make_move(square, letter):
                if print_board:
                    print(f"{letter} makes a move to square {square}")
                    game.print_board()
                    print('') # just an empty line
            
            if game.current_winner:
                if print_board:
                    print(letter + " wins!")
                return letter

            # after we made our move, we need to alternate the letter
            letter = 'O' if letter == 'X' else 'X'
            # above line is comprehension of below code
            # if letter == 'X':
            #     letter = 'O'
            # else: 
            #     letter = 'X'
        
        # tiny break
        time.sleep(0.8)

        if print_board:
            print('It\'s a tie')

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = GeniusComputerPlayer('O')
    game = TicTacToe()
    play(game, x_player, o_player, print_board=True)