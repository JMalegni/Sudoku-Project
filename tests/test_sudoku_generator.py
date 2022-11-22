import unittest
from sudoku_generator import SudokuGenerator

class SudokuGeneratorTest(unittest.TestCase):

    def test_print_board(self):
        gen = SudokuGenerator(9, 0) # 9 rows, no cells removed
        gen.print_board()
        self.assertEqual(None, None)

    def test_valid_in_row(self):
        gen = SudokuGenerator(9, 0)
        self.assertEqual(gen.valid_in_row(4, 9), True)

    def test_valid_in_col(self):
        gen = SudokuGenerator(9, 0)
        self.assertEqual(gen.valid_in_col(4, 9), True)


if __name__ == "__main__":
    # Allows for print() statements to be displayed in console output
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner)
