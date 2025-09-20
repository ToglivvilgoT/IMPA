import sys
import unittest
from unittest.mock import patch
import io

import WeddingofSultan_12582


class TestGetInput(unittest.TestCase):
    @patch('sys.stdin', new_callable=io.StringIO)
    def test_get_input(self, mock_stdin):
        inp = '3\nABBA\nAEFFGGEBDDCCBA\nZAABBZ\n'
        expected = ['ABBA', 'AEFFGGEBDDCCBA', 'ZAABBZ']

        mock_stdin.write(inp)
        mock_stdin.seek(0)

        output = WeddingofSultan_12582.get_input()

        self.assertEqual(output, expected)


class TestSolve(unittest.TestCase):
    def test_example1(self):
        inp = 'AEFFGGEBDDCCBA'
        expected = {
            'A': 2,
            'B': 3,
            'C': 1,
            'D': 1,
            'E': 3,
            'F': 1,
            'G': 1,
        }
        result = WeddingofSultan_12582.solve(inp)

        self.assertEqual(expected, result)

    def test_example2(self):
        inp = 'ZAABBZ'
        expected = {
            'A': 1,
            'B': 1,
            'Z': 2,
        }
        result = WeddingofSultan_12582.solve(inp)

        self.assertEqual(expected, result)

    def test_minimum(self):
        inp = 'ABBA'
        expected = {
            'A': 1,
            'B': 1,
        }
        result = WeddingofSultan_12582.solve(inp)

        self.assertEqual(expected, result)

    def test_depth(self):
        alphabet = 'QWERTYUIOPASDFGHJKLZXCVBNM'
        inp = alphabet + alphabet[::-1]

        expected = {}
        for letter in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            expected[letter] = 2

        expected[alphabet[0]] = 1
        expected[alphabet[-1]] = 1

        result = WeddingofSultan_12582.solve(inp)

        self.assertEqual(expected, result)


class TestPrintDict(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_sorted(self, mock_stdout: io.StringIO):
        inp = {
            'A': 2,
            'B': 4,
        }
        expected = 'A = 2\nB = 4\n'
        
        WeddingofSultan_12582.print_dict(inp)

        result = mock_stdout.getvalue()

        self.assertEqual(expected, result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_unsorted(self, mock_stdout: io.StringIO):
        inp = {
            'B': 1,
            'C': 2,
            'A': 3,
        }
        expected = 'A = 3\nB = 1\nC = 2\n'

        WeddingofSultan_12582.print_dict(inp)

        result = mock_stdout.getvalue()

        self.assertEqual(expected, result)


class TestMain(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('sys.stdin', new_callable=io.StringIO)
    def test_example(self, mock_stdin: io.StringIO, mock_stdout: io.StringIO):
        inp = '2\nAEFFGGEBDDCCBA\nZAABBZ\n'
        expected = 'Case 1\nA = 2\nB = 3\nC = 1\nD = 1\nE = 3\nF = 1\nG = 1\nCase 2\nA = 1\nB = 1\nZ = 2\n'

        mock_stdin.write(inp)
        mock_stdin.seek(0)

        WeddingofSultan_12582.main()

        result = mock_stdout.getvalue()

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

    print('All tests passed!')