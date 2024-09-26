import io
import sys
import unittest
from unittest.mock import patch

import EvenParity_11464


class TestMatrixToInt(unittest.TestCase):
    def test_empty(self):
        inp = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
        expected = 0b000000000
        result = EvenParity_11464.matrix_to_int(inp, len(inp))

        self.assertEqual(expected, result)

    def test_one_grid(self):
        inp = [
            [0, 0, 0],
            [1, 0, 0],
            [0, 0, 0],
        ]
        expected = 0b000001000
        result = EvenParity_11464.matrix_to_int(inp, len(inp))

        self.assertEqual(expected, result)

    def test_impossible_grid(self):
        inp = [
            [1, 1, 1],
            [1, 1, 1],
            [0, 0, 0],
        ]
        expected = 0b000111111
        result = EvenParity_11464.matrix_to_int(inp, len(inp))

        self.assertEqual(expected, result)


class TestGetInput(unittest.TestCase):
    @patch('sys.stdin', new_callable=io.StringIO)
    def test_empty(self, mock_stdin: io.StringIO):
        inp = '1\n3\n0 0 0\n0 0 0\n0 0 0'
        expected = [(0b000000000, 3)]

        mock_stdin.write(inp)
        mock_stdin.seek(0)

        result = EvenParity_11464.get_input()

        self.assertEqual(expected, result)

    @patch('sys.stdin', new_callable=io.StringIO)
    def test_one_grid(self, mock_stdin: io.StringIO):
        inp = '1\n3\n0 0 0\n1 0 0\n0 0 0'
        expected = [(0b000001000, 3)]

        mock_stdin.write(inp)
        mock_stdin.seek(0)

        result = EvenParity_11464.get_input()

        self.assertEqual(expected, result)

    @patch('sys.stdin', new_callable=io.StringIO)
    def test_impossible_grid(self, mock_stdin: io.StringIO):
        inp = '1\n3\n1 1 1\n1 1 1\n0 0 0'
        expected = [(0b000111111, 3)]

        mock_stdin.write(inp)
        mock_stdin.seek(0)

        result = EvenParity_11464.get_input()

        self.assertEqual(expected, result)

    @patch('sys.stdin', new_callable=io.StringIO)
    def test_example_input(self, mock_stdin: io.StringIO):
        inp = '' + \
            '3\n' + \
            '3\n' + \
            '0 0 0\n' + \
            '0 0 0\n' + \
            '0 0 0\n' + \
            '3\n' + \
            '0 0 0\n' + \
            '1 0 0\n' + \
            '0 0 0\n' + \
            '3\n' + \
            '1 1 1\n' + \
            '1 1 1\n' + \
            '0 0 0\n' + \
            ''
        expected = [
            (0b000000000, 3),
            (0b000001000, 3),
            (0b000111111, 3),
        ]

        mock_stdin.write(inp)
        mock_stdin.seek(0)

        result = EvenParity_11464.get_input()

        self.assertEqual(expected, result)


class TestInbounds(unittest.TestCase):
    def test_low_x(self):
        result = EvenParity_11464.is_inbound(-1, 0, 3)
        self.assertFalse(result)

    def test_high_x(self):
        result = EvenParity_11464.is_inbound(3, 0, 3)
        self.assertFalse(result)

    def test_low_y(self):
        result = EvenParity_11464.is_inbound(0, -1, 3)
        self.assertFalse(result)

    def test_high_y(self):
        result = EvenParity_11464.is_inbound(0, 3, 3)
        self.assertFalse(result)

    def test_ok(self):
        result = EvenParity_11464.is_inbound(0, 0, 3)
        self.assertTrue(result)

    def test_bug(self):
        offsets = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        expected = [True, True, False, True]

        for i in range(len(offsets)):
            dx, dy = offsets[i]
            result = EvenParity_11464.is_inbound(2+dx, 1+dy, 3)
            self.assertEqual(expected[i], result)


class TestCoords2Grid(unittest.TestCase):
    def test_width_3(self):
        x, y = 2, 1
        width = 3
        offsets = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        expected = [0b000000100, 0b000010000, 0b001000000, 0b100000000]

        for i in range(len(offsets)):
            dx, dy = offsets[i]
            result = EvenParity_11464.coords2grid(x+dx, y+dy, width)
            self.assertEqual(expected[i], result)


class TestCheckNeighbours(unittest.TestCase):
    def test_empty_3x3(self):
        grid = 0b000000000
        expected = [
            (0, [(1, 0), (0, 1)]),
            (0, [(0, 0), (2, 0), (1, 1)]),
            (0, [(1, 0), (2, 1)]),
            (0, [(0, 0), (1, 1), (0, 2)]),
            (0, [(1, 0), (0, 1), (2, 1), (1, 2)]),
            (0, [(2, 0), (1, 1), (2, 2)]),
            (0, [(0, 1), (1, 2)]),
            (0, [(1, 1), (0, 2), (2, 2)]),
            (0, [(2, 1), (1, 2)]),
        ]
        
        for y in range(0):
            for x in range(0):
                result = EvenParity_11464.check_neighbours(grid, x, y, 3)
                self.assertEqual(result, expected[y*3 + x])

    def test_one_3x3(self):
        grid = 0b000100000
        expected = [
            (0, [(1, 0), (0, 1)]),
            (0, [(0, 0), (2, 0), (1, 1)]),
            (1, [(1, 0)]),
            (0, [(0, 0), (1, 1), (0, 2)]),
            (1, [(1, 0), (0, 1), (1, 2)]),
            (0, [(2, 0), (1, 1), (2, 2)]),
            (0, [(0, 1), (1, 2)]),
            (0, [(1, 1), (0, 2), (2, 2)]),
            (1, [(1, 2)]),
        ]
        
        for y in range(3):
            for x in range(3):
                result = EvenParity_11464.check_neighbours(grid, x, y, 3)
                self.assertEqual(result, expected[y*3 + x])


class TestCheckGrid(unittest.TestCase):
    """ Runs tests for check_grid() function """

    def test_inpossible(self):
        """ Tests board which cant be solved """
        inp = 0b111111000
        width = 3
        expected = False
        result = EvenParity_11464.check_grid(inp, width)

        self.assertEqual(expected, result)

    def test_complete(self):
        """ Tests board which is already solved """
        inp1 = 0b000000000
        inp2 = 0b010101010
        width = 3
        expected = True
        result1 = EvenParity_11464.check_grid(inp1, width)
        result2 = EvenParity_11464.check_grid(inp2, width)

        self.assertEqual(expected, result1)
        self.assertEqual(expected, result2)

    def test_board_returns(self):
        """ Tests that the function returns correct next boards """

        inps = [
            (0b000001000, 3),
            (0b010001010, 3),
        ]
        expected = [{
                inps[0][0] + 0b000000010,
                inps[0][0] + 0b000100000,
                inps[0][0] + 0b010000000,
            }, {
                inps[1][0] + 0b000100000,
            },
        ]

        for i in range(len(inps)):
            result = EvenParity_11464.check_grid(*inps[i])

            self.assertEqual(expected[i], result)


class TestSolve(unittest.TestCase):
    """ Tests the solve() function """

    def test_empty(self):
        inp = 0b000000000
        width = 3
        expected = 0
        result = EvenParity_11464.solve(inp, width)

        self.assertEqual(expected, result)

    def test_completeble(self):
        inp = 0b000001000
        width = 3
        expected = 3
        result = EvenParity_11464.solve(inp, width)

        self.assertEqual(expected, result)

    def test_empty(self):
        inp = 0b000111111
        width = 3
        expected = -1
        result = EvenParity_11464.solve(inp, width)

        self.assertEqual(expected, result)


class TestMain(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('sys.stdin', new_callable=io.StringIO)
    def test_example(self, mock_stdin: io.StringIO, mock_stdout: io.StringIO):
        inp = \
            '3\n' + \
            '3\n' + \
            '0 0 0\n' + \
            '0 0 0\n' + \
            '0 0 0\n' + \
            '3\n' + \
            '0 0 0\n' + \
            '1 0 0\n' + \
            '0 0 0\n' + \
            '3\n' + \
            '1 1 1\n' + \
            '1 1 1\n' + \
            '0 0 0\n'
        
        expected = \
            'Case 1: 0\n' + \
            'Case 2: 3\n' + \
            'Case 3: -1\n'
        
        mock_stdin.write(inp)
        mock_stdin.seek(0)

        EvenParity_11464.main()

        result = mock_stdout.getvalue()

        self.assertEqual(expected, result)
        


if __name__ == '__main__':
    unittest.main()

    print('All tests passed!')