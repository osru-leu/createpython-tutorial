#def check_for_winner(a, b, c):
board = [
        [ '1',  '2' , '3' ],
        [ '4',  '5' , '6' ],
        [ '7',  '8' , '9' ],
        ]



def player_x_turn():

    print('Where would you like to place "X"?')
    player_x = 'X'
    row_x = int(input('Row?'))
    column_x = int(input('Column?'))
    game = game_board(player=player_x, row=row_x, column=column_x )
    return game
    

# REDUCE THE PLAYER TURNS TO ONE FUNCTION
def player_o_turn():

    print('Donde "O"?')
    player_o = 'O'
    row_o = int(input('Row?'))
    column_o = int(input('Column?'))
    return game_board(player=player_o, row=row_o, column=column_o )

def game_board(player=(player_x_turn(), player_o_turn()), row=0, column=0):
    print('   0  1  2 - column')
    
    board[row][column] = player
    for item in board:
        print(item)
    return item
    
    
if __name__ == "__main__":
    
    
    while True:
        #print('**********while loop iteration*********')
        BOARD = game_board(player_o_turn, player_x_turn)
        # board = [
        #     [ '1',  '2' , '3' ],
        #     [ '4',  '5' , '6' ],
        #     [ '7',  '8' , '9' ],
        #     ]
      
        player_x_turn()
        player_o_turn()
     
        
        
   