import random

def show():
    print(board [0],'|',board [1],'|',board [2])
    print('----------')
    print(board [3],'|',board [4],'|',board [5])
    print('----------')
    print(board [6],'|',board [7],'|',board [8])
    
def is_winner(player_being_checked):
    b = board
    win = False
    if b[0] == player_being_checked:
        if (b[1], b[2]) == (player_being_checked, player_being_checked):
            win = True
        if (b[3], b[6]) == (player_being_checked, player_being_checked):
            win = True
        if (b[4], b[8]) == (player_being_checked, player_being_checked):
            win = True
    if b[4] == player_being_checked:
        if (b[1], b[7]) == (player_being_checked, player_being_checked):
            win = True
        if (b[3], b[5]) == (player_being_checked, player_being_checked):
            win = True
        if (b[6], b[2]) == (player_being_checked, player_being_checked):
            win = True
    
    if b[8] == player_being_checked:
        if (b[6], b[7]) == (player_being_checked, player_being_checked):
            win = True
        if (b[2], b[5]) == (player_being_checked, player_being_checked):
            win = True
 
    return win

def play():
    while True:
        spot = int(input('Select a spot: '))
         
        if board[spot] not in 'xo':
            board[spot] = 'x'
            
            if is_winner('x'):
                
                print('Congratulations you win! :)')
                break


            while True:
                random.seed()
                opponent = random.randint(0,8)

                if board[opponent] not in 'xo':
                    board[opponent] = 'o'
                    break
            if is_winner('o'): # now inside is_winner the variable p = 'o'
                print('Computer wins :(')
                break
        else:
            print('this spot is taken')
        show()

if __name__ == '__main__':
    print('Tic Tac Toe. In this version of Tic Tac Toe you are X and the computer is O. To place your X piece type a number from 0-8 to play it on the board. Enjoy') 
    board = [str(x) for x in range(9)]
    play_again = 'y'
    while play_again.startswith('y'):
        show()
        play()
        play_again = input('Do you want to play again? ')
        board = [str(x) for x in range(9)]
            
    print('Good Bye')
    