import unittest
from sudoku_generator import SudokuGenerator

class SudokuGeneratorTest(unittest.TestCase):

    def test_print_board(self):
        gen = SudokuGenerator(9, 0) # 9 rows, no cells removed
        gen.print_board()
        self.assertEqual(None, None)

    '''def test_valid_in_row(self):
        gen = SudokuGenerator(9, 0)
        if gen.valid_in_row(0, 1): # desired row, num to check for
            print("Valid Input")
        elif not gen.valid_in_row(0, 1):
            print("invalid")

    def test_valid_in_col(self):
        gen = SudokuGenerator(9, 0)
        if gen.valid_in_col(0, 0): # desired column, num to check for
            print("Valid Input col")
        elif not gen.valid_in_col(0, 0):
            print("invalid col")'''


if __name__ == "__main__":
    # Allows for print() statements to be displayed in console output
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner)
