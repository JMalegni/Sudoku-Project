import unittest
import sudoku_generator as sudoku_generator
from sudoku_generator import SudokuGenerator

class SudokuGeneratorTest(unittest.TestCase):

    def test_valid_in_row(self):
        print("===test_valid_in_row===")
        gen = SudokuGenerator(9, 0)
        self.assertEqual(gen.valid_in_row(4, 9), True)

    def test_valid_in_col(self):
        print("===test_valid_in_col===")
        gen = SudokuGenerator(9, 0)
        self.assertEqual(gen.valid_in_col(4, 9), True)

    def test_valid_in_box(self):
        print("===test_valid_in_box===")
        gen = SudokuGenerator(9, 0)

        gen.board[1][1] = 3
        #  gen.print_board()

        validity = gen.valid_in_box(0, 0, 3) # check box starting at (0, 0) for 3, or the changed value
        self.assertEqual(validity, False) # validity will be False if value is matched

    def test_is_valid(self):
        print("===test_is_valid===")
        gen = SudokuGenerator(9, 0)

        gen.board[1][1] = 3
        #  gen.print_board()

        validity = gen.is_valid(2, 2, 3) # check row 2, col 2, and box at (0,0)
        self.assertEqual(validity, False)

    def test_is_valid_2(self):
        print("===test_is_valid_2===")
        gen = SudokuGenerator(9, 0)

        gen.board[7][7] = 3
        #  gen.print_board()

        validity = gen.is_valid(6, 6, 3) # check row 6, col 6, and box at (6,6)
        self.assertEqual(validity, False)

    def test_fill_box(self):
        print("===test_fill_box===")
        gen = SudokuGenerator(9, 0)

        gen.fill_box(3,3) # row_start and col_start are the arguments
        gen.print_board()

        self.assertEqual(True, True)

    def test_fill_diagonal(self):
        print("===test_fill_diagonal===")
        gen = SudokuGenerator(9, 0)

        gen.fill_diagonal()
        gen.print_board()

        self.assertEqual(True, True)

    def test_fill_values(self):
        print("===test_fill_values===")
        gen = SudokuGenerator(9, 0)
        gen.print_board()
        gen.fill_values()
        gen.print_board()

        self.assertEqual(True, True)

    def test_remove_cells(self):
        print("===test_remove_cells===")
        gen = SudokuGenerator(9, 30) # 9x9 board, 30 cells removed
        gen.fill_values()
        gen.remove_cells()
        gen.print_board()

        self.assertEqual(True, True)

    def test_generate_sudoku(self):
        print("===test_generate_sudoku===")
        board = sudoku_generator.generate_sudoku(9, 30)
        print(board) # prints puzzle
        '''
        Not really sure how the solution is saved, the board retrieved after remove_cells() is called
        rewrites the list that is the solution, instead of apphending it... should we make a new function inside
        of sudoku_generator?
        
        '''


        self.assertEqual(True, True)

    def test_generate_sudoku_2(self):
        print("===test_generate_sudoku_2===")
        board = sudoku_generator.generate_sudoku_2(9, 30)
        print(board)  # prints puzzle

        self.assertEqual(True, True)



if __name__ == "__main__":
    # Allows for print() statements to be displayed in console output
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner)
