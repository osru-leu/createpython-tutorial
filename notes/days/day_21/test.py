import numpy as np
        # board display 
        # ask for character placement
        # allow exit
        # take character placement and put it on the board
        # display placement of character on the board
        # player 2 turn
        # repeat
        # look for a winner
        # apply checks for incorrect entry
        # exit
# ANOTHER BOARD SETUP USING NUMPY BELOW
# >>>a = np.arange(9).reshape(3, 3)
# >>>a
# array([[0, 1, 2],
#         3, 4, 5],
#         6, 7, 8]])
board = [
        [ '1',  '2' , '3' ],
        [ '4',  '5' , '6' ],
        [ '7',  '8' , '9' ],
        ]

def board_display():
    for item in board:
        print(item)

def col_win(move):
    while True:
        check = np.any((np.all(board == move, axis=0)))
        return check
         

def exit_game(move):

    if move == 'E':
        print('Deuce Deuce')
        exit()

def player_move_x(move):

    for row in range(3):
        for col in range(3):
            if board[row][col] == move:
                board[row][col] = 'X'
            
    return board_display()

def player_move_o(move):

    for row in range(3):
        for col in range(3):
            if board[row][col] == move:
                board[row][col] = 'O'            
    return board_display()

def check_rows(move):

    for row in board:
        if len(set(row)) == 1:
            print('Horz Weeeeiner!')
            return row [0]
    return

def check_diags(board):

    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return board[0][0]

    if len(set([board[i][len(board)-i-1] for i in range(len(board))]))== 1:
        print('winner')
        return board[0][len(board)-1]

    return 

def check_win(board):
    for newBoard in [board, np.transpose(board)]:
        result = check_rows(newBoard)
        if result:
            return result
    return check_diags(board)

if __name__ == "__main__":
    
    while True:
        
        print("Welcome to Tic Tac Toe! press 'E' at and time to exit")
        board_display()
        
        MOVE = str(input('Where would you like to place your player "X" 1-9?')).upper()
        player_move_x(MOVE)
        check_win(MOVE)
        col_win(MOVE)
        # check_rows(MOVE)
        # check_diags(MOVE)
        exit_game(MOVE)
    
        
        MOVE = str(input('Where would you like to place your player "O" 1-9?')).upper()
        player_move_o(MOVE)
        check_win(MOVE)
        # check_rows(MOVE)
        # check_diags(MOVE)
        
        exit_game(MOVE)
        
    
        #player_move()

    # def check_for_winner(row):
    # for row in range(3):
    #     if len(row[0]) == 'X':
    #         return print('winner')
    #     else:
    #         return print('nope')
    #     # if row[0] == len(row[0]) and row[0] == board.count([0]):
    #     #     print('Winner damnit')
    #     # if row[0] == len(row[0]) and row[0] != [0]:
    #     #     return row
    # return
    # # for row in board:
    # #     if len(set(row)) == 1:
    # #         return row[0]
    # #     return 0

    # # if board.count()== 'X'> 3:
    # #     print(winner)