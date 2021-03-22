import random
class TicTacToe:
    def __init__ (self):
        self.board = ['1','2','3','4','5','6','7','8','9']
        print('''
   |   |
 1 | 2 | 3 
   |   |
-----------
   |   |
 4 | 5 | 6
   |   |
-----------
   |   |
 7 | 8 | 9
   |   |
        ''')
    def display (self):
        print('   |   |')
        print(' ' + self.board[0] + ' | ' + self.board[1] + ' | ' + self.board[2])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[3] + ' | ' + self.board[4] + ' | ' + self.board[5])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[6] + ' | ' + self.board[7] + ' | ' + self.board[8])
        print('   |   |')
    def chooseFirstPlayer(self):
        n = random.randint(0,1)
        if n:
            return '1'
        return '2'
    def getMove (self,player):
        if player == '1':
            print("Player 1, Take a move(1-9):")
            move = str(input())
            while ((move != '1') and (move != '2') and (move != '3') and (move != '4') and (move != '5') and (move != '6') and (move != '7') and (move != '8') and (move != '9')):
                print("Invalid move. Please try again.") 
                move = (input())
            move = int(move)
            while (self.board[move-1] == 'O') or (self.board[move-1] == 'X'):
                print("Invalid move. Please try again.") 
                move = (input())
                move = int(move)
            self.board[move-1] = 'X'
        else:
            print("Player 2, Take a move(1-9):")
            move = str(input())
            while ((move != '1') and (move != '2') and (move != '3') and (move != '4') and (move != '5') and (move != '6') and (move != '7') and (move != '8') and (move != '9')):
                print("Invalid move. Please try again.") 
                move = (input())
            move = int(move)
            while (self.board[move-1] == 'O') or (self.board[move-1] == 'X'):
                print("Invalid move. Please try again.") 
                move = (input())
                move = int(move)
            self.board[move-1] = 'O'
    def winner (self,player):
        if player == '1':
            ox = 'X'
        else:
            ox = 'Y'
        return ((self.board[7] == ox and self.board[8] == ox and self.board[9] == ox) or # across the top
        (self.board[3] == ox and self.board[4] == ox and self.board[5] == ox) or # across the middle
        (self.board[6] == ox and self.board[7] == ox and self.board[8] == ox) or # across the bottom
        (self.board[0] == ox and self.board[1] == ox and self.board[2] == ox) or # across the top
        (self.board[0] == ox and self.board[3] == ox and self.board[6] == ox) or # down the left side
        (self.board[1] == ox and self.board[4] == ox and self.board[7] == ox) or # down the middle
        (self.board[2] == ox and self.board[5] == ox and self.board[8] == ox) or # down the right side
        (self.board[2] == ox and self.board[4] == ox and self.board[6] == ox) or # diagonal
        (self.board[0] == ox and self.board[4] == ox and self.board[8] == ox))   # diagonal
    def endGame (self):
        if self.winner('1'):
            print("Player 1 Wins!")
            return True
        elif self.winner('2'):
            print("Player 2 Wins!")
            return True
        else:
            for i in self.board:
                if i != 'O' and i != 'X':
                    return False
        print("Its a tie!")
        return True


def playGame ():
    ttt = TicTacToe()
    print("Welcome to Tic Tac Toe!")
    while True:
        player = ttt.chooseFirstPlayer()
        print("Player " + player + " will go first.")
        while True:
            if ttt.endGame():
                break
            ttt.getMove(player)
            ttt.display()
            if player == '1':
                player = '2'
            else:
                player = '1'
        print("Would you like to play again?(y/n)")
        yn = input()
        while yn != 'y' and yn != 'n':
            print("Invalid answer. Make sure your answer is y or n. Would you like to play again?(y/n)")
            yn = input()
        if yn == 'n':
            break

    print("Goodbye!")



playGame()