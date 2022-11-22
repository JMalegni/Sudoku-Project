import unittest
from sudoku_generator import SudokuGenerator

class SudokuGeneratorTest(unittest.TestCase):

    def test_valid_in_row(self):
        gen = SudokuGenerator(9, 0)
        self.assertEqual(gen.valid_in_row(4, 9), True)

    def test_valid_in_col(self):
        gen = SudokuGenerator(9, 0)
        self.assertEqual(gen.valid_in_col(4, 9), True)

    def test_valid_in_box(self):
        gen = SudokuGenerator(9, 0)

        gen.board[1][1] = 3
        gen.print_board()
        
        validity = gen.valid_in_box(0, 0, 3) # check box starting at (0, 0) for 3, or the changed value
        self.assertEqual(validity, False) # validity will be False if value is matched


if __name__ == "__main__":
    # Allows for print() statements to be displayed in console output
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner)
