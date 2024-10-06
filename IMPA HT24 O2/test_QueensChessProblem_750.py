import QueensChessProblem_750

import unittest
from unittest.mock import patch

from sys import stdin, stdout
from io import StringIO


class TestPlaceQueens(unittest.TestCase):
    def test_all(self):
        all_possible = QueensChessProblem_750.place_queens(set())

        possible_input = [(x, y) for x in range(8) for y in range(8)]

        for inp in possible_input:
            result = QueensChessProblem_750.place_queens({inp})
            expected = [board for board in all_possible if inp in board]

            for elem in result:
                self.assertIn(elem, expected)
            for elem in expected:
                self.assertIn(elem, result)


if __name__ == '__main__':
    unittest.main()