import numpy as np

def isPossible(board, num, row, col):               #checks if a number can go into a specific spot
        
    col_nums = [board[n][col] for n in range(9)]    # get a single column from the board
    if num in col_nums:                             # if the number appears in the same column, can't go here
        return False

   
    row_nums = board[row]                           # get a single row from the board
    if num in row_nums:                             # if the number appears in the same row, can't go here
        return False


    square_row = (row // 3) * 3                     # get start point for 3x3 grid row
    square_col = (col // 3) * 3                     # ... and for column

    for i in range(square_row, square_row + 3):     # check the 3x3 box for equal value
        for j in range(square_col, square_col + 3):
            if board[i][j] == num:
                return False
    return True

def solve(board):
    row, col = find_empty(board)

    if col == None:
        return True

    for num in range(1,10):                         # try all numbers 1-9 
        if isPossible(board, num, row, col):        # run them through isPossible() function
            board[row][col] = num 
            if solve(board):                        # recursively use solve to check various board spots
                return True                         
        board[row][col] = 0
    return False                                    # go back a level if no values work for empty spot
                                                    # if no numbers work, one of the previous choices must have led
                                                    # down bad path


def find_empty(board):                              # find next empty board space

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None


board = [list(input()) for _ in range(9)]

for i in range(9):
    for j in range(9):
        if board[i][j] == "*":
            board[i][j] = 0
        else:
            board[i][j] = int(board[i][j])


if (solve(board)):
    for i in range(9):
        print("")
        for j in range(9):
            print(board[i][j], end = '')


else:
    print("-1")