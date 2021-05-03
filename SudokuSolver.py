def find_next_empty(puzzle):
    # finds the next row,col on the table to fill in
    for r in range (9):
        for c in range (9):
            if puzzle [r][c] == -1:
                return r,c
    return None,None #if no spaces in the puzzle are empty

def is_valid(puzzle, guess, row, column):
    # figures out if a guess is valid

    #checks the row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    #checks the columns
    #col_vals = []
    #for i in range (9):
    # col_vals.append(puzzle[i][column])
    col_vals = [puzzle[i][column] for i in range (9)]
    if guess in col_vals:
        return False
    #checks the 3x3 square
    row_start = (row // 3) *3
    col_start = (column //3)*3
    for r in range (row_start, row_start +3):
        for c in range (col_start, col_start + 3):
            if puzzle [r][c]== guess:
                return False
    return True


def solve_sudoku(puzzle):
        # solves sudoku using a backtracking technique
        # our puzzle will be a list of lists and we will return weather a solution exists
        # mutates puzzle to be the solution (if the solution exists)

        # step 1 - choose somewhere on the puzzle to go to/ make a guess
        row, col = find_next_empty(puzzle)

        #validation to see if we have complete the puzzle
        if row is None :
            return True

        #if there is a place to put our guess we want to come up with a random number to put our guess in
        for guess in range (1,10):
            # check if its a valid guess
            if is_valid(puzzle, guess, row, col):
                puzzle[row][col] = guess
        # recurively call our function
        if solve_sudoku(puzzle):
            return True
        # if the guess is not valid or if the guess does not solve the puzzle we need to keep trying
        puzzle [row][col]= -1
    #if none of the number we try actually work, then the puzzle is unsolvable
        return False








