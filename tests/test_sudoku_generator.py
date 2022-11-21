import unittest
from sudoku_generator import SudokuGenerator

class SudokuGeneratorTest(unittest.TestCase):

    def test_get_board(self):
        # currently testing printed output
        print("Empty board:")
        # board is printed when get_board is called inside SudokuGenerator.__init__()
        gen = SudokuGenerator(9, 0)
        gen.print_board()
        self.assertEqual(None, None)

if __name__ == "__main__":
    # Allows for print() statements to be displayed in console output
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner)
