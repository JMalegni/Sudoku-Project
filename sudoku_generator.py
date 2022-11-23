import math,random

"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""

class SudokuGenerator:
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length

	Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

	Return:
	None
    '''
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.box_length = int(math.sqrt(row_length)) # 9^(1/2) = 3, must not be a float to prevent bugs
        self.board = self.get_board()

    '''
	Returns a 2D python list of numbers which represents the board

	Parameters: None
	Return: list[list]
    '''
    def get_board(self):
        # Board (the puzzle itself) needs to be constructed from this function

        # Create 2D list to represent board, inner lists are rows
        board = [[] for i in range(self.row_length)]
        for row in board:
            row_vals = [0 for i in range(self.row_length)]
            row.extend(row_vals)

        return board

    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

	Parameters: None
	Return: None
    '''
    def print_board(self):
        print() # print newline
        for row_index in range(len(self.board)):
            for digit_index, digit in enumerate(self.board[row_index]):
                if digit == 0:
                    print(" ", end=" ") # print blank space
                else:
                    print(digit, end=" ")

                # Start printing next row
                if (digit_index + 1) == 9:
                    print()
                    continue

                # Seperate every 3 columns
                if (digit_index + 1) % 3 == 0:
                    print("|", end=" ")

            # Seperate every 3 rows
            if (row_index + 1) % 3 == 0 and (row_index + 1) != 9:
                print("-" * (9 + 9 + 3))

    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row
	
	Return: boolean
    '''
    def valid_in_row(self, row, num, digit_start=0, row_length=9):
        #need to iterate through the selected row
        # digit_start and row_length are used to make using valid_in_box work more easily

        for i in range(row_length):
            if self.board[row][i + digit_start] == num:
                return False
        return True

    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column
	
	Return: boolean
    '''
    def valid_in_col(self, col, num, digit_start=0, col_length=9):
        # need to iterate through the selected column
        # row length should be fine since it's a 9x9 grid
        # digit_start and col_length are used to make using valid_in_box work more easily
        
        for i in range(col_length):
            if self.board[i+ digit_start][col] == num:
                return False
        return True

    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box

	Return: boolean
    '''
    def valid_in_box(self, row_start, col_start, num, box_length=3):
        # return False if a match is found within any of the next 3 rows/cols. only check up until the box's size (so rows and cols only check 3 spaces each) 
        #  print(f"checking box at ({col_start},{row_start})")

        for i in range(box_length):
            # if we check a box starting at row 3, col 0, we need to start our col checks at digit 3, which is also row_start
            if self.valid_in_row(row_start + i, num, col_start, box_length) == False:
                return False
            if self.valid_in_col(col_start + i, num, row_start, box_length) == False:
                return False
        # If no match is found:
        return True

    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    '''
    def is_valid(self, row, col, num):
        # find which box num is in using row and col, get coordinates of starting position
        box_x = int(col // self.box_length)
        box_col = box_x * 3
        box_y = int(row // self.box_length)
        box_row = box_y * 3

        if self.valid_in_row(row, num) == False:
            return False
        elif self.valid_in_col(col, num) == False:
            return False
        elif self.valid_in_box(box_row, box_col, num) == False:
            return False

        # If no match is found:
        return True

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

    Parameters:
    row_start and col_start are the starting indices of the box to check
    i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

    Return: None
     '''
    def fill_box(self, row_start, col_start):
        ran_list = []

        for i in range(3):
            for j in range(3):
                #get random number from [1,9]
                ran_num = random.randint(1, 9)
                #makes sure the number hasn't been used already
                while ran_num in ran_list:
                    ran_num = random.randint(1, 9)

                #change value of board position to the random number that hasn't been used yet
                self.board[row_start+i][col_start+j] = ran_num

                ran_list.append(ran_num)

    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

    Parameters: None
    Return: None
    '''
    def fill_diagonal(self):
        #call fill_box for the top left, middle, and bottom right boxes
        for i in range(0, 9, 3):
            self.fill_box(i, i)

    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled
	
	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    '''
    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

	Parameters: None
	Return: None
    '''
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called
    
    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''
    def remove_cells(self):
        pass

'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board
