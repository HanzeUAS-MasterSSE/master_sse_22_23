#import necessary modules
import numpy as np

#declare size of board 
ROWS = 6
COLUMNS = 7

#create the playing board 
board = np.zeros((6,7))

#a flipped board is easier to work with (incrementally speaking)    
def print_board(board):
    print(np.flip(board,0))

#drop a piece onto the board 
def drop_piece(board,row,col,piece):
    board[row][col]= piece

#get next available row you can drop a piece into 
def get_next_open_row(board,col):
    for r in range(ROWS):
        if board[r][col]==0:
            return r

#check if 4 pieces are the same next to each other
def check_for_winner(board, piece):
    # Check all rows (column by column)
    for c in range(COLUMNS-3):
        for r in range(ROWS):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
 
    # Check all columns (row by row)
    for c in range(COLUMNS):
        for r in range(ROWS-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
 
    # Check positively sloped diagonals (increase in both rows and columns)
    for c in range(COLUMNS-3):
        for r in range(ROWS-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
 
    # Check negatively sloped diagonals (increase columns, reduce rows)
    for c in range(COLUMNS-3):
        for r in range(3, ROWS):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

#turn computations
def play_turn(board, col, piece):
    global game_over
    global turn
    if board[5][col]==0: #check that top row is not full
        row = get_next_open_row(board,col) 
        drop_piece(board,row,col,piece)

        if check_for_winner(board, piece):
            #show final board
            print_board(board)
            #declare winner
            print (f"Game Over! Player {piece} wins!")
            game_over = True

    else:
        print (f"Column is full, Player {piece}, please play again")
        turn -= 1

#set starter game variables
game_over = False
turn = 0
 
while not game_over:
    #Print the board
    print_board(board)

    #Player 1's turn
    if turn == 0:

        piece = 1 #Piece for Player 1
        col = int(input("Player 1, Make your Selection(0-6):"))
        play_turn(board, col, piece)
         
    #Player 2's turn
    else:
        piece = 2 #Piece for Player 2
        col = int(input("Player 2, Make your Selection(0-6):"))
        play_turn(board, col, piece)

    turn += 1
    turn = turn % 2