import numpy as np

def checkRows(board):
    for row in board:
        if len(set(row)) == 1:
            return row[0]
    return 0

def checkDiagonals(board):
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return board[0][0]
    if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
        return board[0][len(board)-1]
    return 0

def checkWin(board):
    #transposition to check rows, then columns
    for newBoard in [board, np.transpose(board)]:
        result = checkRows(newBoard)
        if result:
            return result
    return checkDiagonals(board)


a = [['X', 'A', 'X'],
     ['A', 'X', 'A'],
     ['A', 'X', 'A']]

print(checkWin(a))

# def board_display():

#      for pos in BOARD:
#             if QUAD_SELECT == pos:
#                 pos = 'X'
#                 print('Board')
#                 for item in BOARD:
#                     print('|', item[0],''*(1-len(str(item[0]))),
#                           '|', item[1],''*(1-len(str(item[1]))),
#                           '|', item[2],''*(1-len(str(item[2]))),'|')
#             return BOARD




# while True:
        
#     BOARD = [
#         [  1, 2, 3  ],
#         [  4, 5, 6  ],
#         [  7, 8, 9  ],
#         ] 
#     QUAD_SELECT = int(input('''Where would you like to place your character?
#                                 [  1  |  2  |  3  ]
#                                 [  4  |  5  |  6  ]
#                                 [  7  |  8  |  9  ]    '''))
#     #board_display()
    
#     if QUAD_SELECT in BOARD == True:
#         print('yes')
#     else:
#         print('no bitch')
#     for i in BOARD[0][0:0]: # translate this to the whole board
#         if QUAD_SELECT == 1: # if quad select == item in board
#             BOARD[0][0] = 'x' #item in BOARD = 'X'
#             print(BOARD) 
#             for item in BOARD:
#                 print('|', item[0],''*(1-len(str(item[0]))),
#                         '|', item[1],''*(1-len(str(item[1]))),
#                         '|', item[2],''*(1-len(str(item[2]))),'|')
#         continue

# # take the value of QUAD_SELECT and push it through BOARD
#     #SET EACH LIST EQUAL TO ITS CORRISPONDING NUMBERS?
#     print('reached code')
#     for row in BOARD:
#         for item in row:
#             print(item)
#     if item in row == QUAD_SELECT:
#         print('|', item[0],''*(1-len(str(item[0]))),
#                 '|', item[1],''*(1-len(str(item[1]))),
#                 '|', item[2],''*(1-len(str(item[2]))),'|')
#         print(BOARD)
#         for item in BOARD:
#             print('|', item[0],''*(1-len(str(item[0]))),
#                     '|', item[1],''*(1-len(str(item[1]))),
#                     '|', item[2],''*(1-len(str(item[2]))),'|')
    
# # WEINERS BOARD DEF #########################
# def game_board(player=0, row=0, column=0):
#     print('   0  1  2 - column')
    
#     board[row][column] = player
    
#     for count, row in enumerate(board):
#         print(count, row)

#     return board

# def player_select(player_1, player_2):
#     if character == 'X':
#         player_1 = 'X'
#     player_2 = 'O'

#     return character


#     character = input("Would you like to be 'X's or 'O's?")
#     player_select(player_1=character, player_2=character)