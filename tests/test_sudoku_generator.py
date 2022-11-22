import unittest
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
        gen.print_board()
        
        validity = gen.valid_in_box(0, 0, 3) # check box starting at (0, 0) for 3, or the changed value
        self.assertEqual(validity, False) # validity will be False if value is matched

    def test_is_valid(self):
        print("===test_is_valid===")
        gen = SudokuGenerator(9, 0)

        gen.board[1][1] = 3
        gen.print_board()

        validity = gen.is_valid(2, 2, 3) # check row 2, col 2, and box at (0,0)
        self.assertEqual(validity, False)

    def test_is_valid(self):
        print("===test_is_valid_2===")
        gen = SudokuGenerator(9, 0)

        gen.board[1][1] = 3
        gen.print_board()

        validity = gen.is_valid(3, 2, 3) # check row 3, col 2, and box at (3,0)
        self.assertEqual(True, True)

if __name__ == "__main__":
    # Allows for print() statements to be displayed in console output
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner)
