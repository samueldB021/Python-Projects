'''SUDOKU SOLVER

We are building a Python file that can solve a Sudoku after being given a set of inputs.
This will be done using backtracking'''

# The board to be solved
board = [[0, 1, 0, 0, 6, 0, 0, 0, 4],
        [0, 0, 4, 0, 1, 5, 0, 6, 0],
        [0, 6, 0, 0, 3, 0, 8, 0, 0],
        [5, 0, 9, 7, 0, 0, 0, 0, 0],
        [1, 0, 3, 0, 5, 0, 0, 0, 0],
        [7, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 1],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 4, 0]]

""" empty_square: checking if there are empty square(s) left on the board and returning co-ordinates of them if there are """
def empty_square (board):
    for i in range (len(board)): #row
        for j in range (len(board[0])): #column
            if board[i][j] ==0:
                return (i, j) #row, column
    return None

""" is_valid: checking if the number filled in is valid or not
For a sudoku game, we need to make sure the same number has not been repeated in its corresponding row, column or 3x3 square """
def is_valid (board, value, pos):
    # checking its corresponding column
    for i in range (len(board)):
        if board[i][pos[1]] == value and pos[0] != i:
            return False

    # Checking its corresponding row
    for j in range (len(board[0])):
        if board[pos[0]][j] == value and pos[1] != j:
            return False
    # Checking its corresponding square

    # Dividing by 3 will give either a 0, 1 or 2.
    # We need to loop through those 3 numbers which give off the same number as our row
    row = pos[0] // 3
    column = pos[1] // 3
    for i in range (row*3, row*3+3):
        for j in range (column*3, column*3+3):
            if board[i][j] == value and (i,j) != pos:
                return False
    return True

""" solve_sudoku: The main function which handles the solving of the sudoku, returns the completed 9x9 square"""
def solve_sudoku(board):
    # check if there are any empty squares left
    if not empty_square(board):
        return True
    else:
        row, col = empty_square(board)

    # running through possible values and checking the validity
    for i in range (1,10):
        if is_valid(board, i, (row, col)):
            # if valid insert the value in the position
            board[row][col] = i

            # the function is back recalled to solve another square, until it reaches a point where all the solutions are impossible
            # in which case, we reset the value to zero and try another value from the for loop
            if solve_sudoku(board):
                return True
        
            board[row][col] = 0
    
    return False


    pass
def print_board(board):
    for i in range(len(board)):
        if i%3 == 0 and i!=0:
            print('___________________')
    
        for j in range( len(board[0])):
            if j%3 ==0 and j!=0:
                print("|", end = '')
            if j == 8: print(board[i][j])
            else: print(str(board[i][j])+' ', end='')


print_board(board)
solve_sudoku(board)
print("\nAfter Solving:")
print_board(board)