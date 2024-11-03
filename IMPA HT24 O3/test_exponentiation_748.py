import unittest
from unittest.mock import patch

import sys
import io

from exponentiation_748 import *


class TestGetInput(unittest.TestCase):
    @patch('sys.stdin', new_callable=io.StringIO)
    def test_empty(self, mock_stdin: io.StringIO):
        self.assertEqual(get_input(), [])

    @patch('sys.stdin', new_callable=io.StringIO)
    def test_one(self, mock_stdin: io.StringIO):
        mock_stdin.write('123.45 12')
        mock_stdin.seek(0)

        self.assertEqual(get_input(), [('12345', 12)])

    @patch('sys.stdin', new_callable=io.StringIO)
    def test_multiple(self, mock_stdin: io.StringIO):
        mock_stdin.write('123.45 12\n23.456  1\n.34567 25')
        mock_stdin.seek(0)

        self.assertEqual(get_input(), [('12345', 12), ('23456', 1), ('34567', 25)])

    @patch('sys.stdin', new_callable=io.StringIO)
    def test_leadin_decimal(self, mock_stdin: io.StringIO):
        mock_stdin.write('123.45 12\n23.456  1\n.34567 25')
        mock_stdin.seek(0)

        self.assertEqual(get_input(), [('12345', 12), ('23456', 1), ('34567', 25)])

    @patch('sys.stdin', new_callable=io.StringIO)
    def test_trailing_decimal(self, mock_stdin: io.StringIO):
        mock_stdin.write('123.45 12\n23.456  1\n.34567 25')
        mock_stdin.seek(0)

        self.assertEqual(get_input(), [('12345', 12), ('23456', 1), ('34567', 25)])

    @patch('sys.stdin', new_callable=io.StringIO)
    def test_leadin_zeros(self, mock_stdin: io.StringIO):
        mock_stdin.write('123.45 12\n23.456  1\n.34567 25')
        mock_stdin.seek(0)

        self.assertEqual(get_input(), [('12345', 12), ('23456', 1), ('34567', 25)])

    @patch('sys.stdin', new_callable=io.StringIO)
    def test_trailing_zeros(self, mock_stdin: io.StringIO):
        mock_stdin.write('123.45 12\n23.456  1\n.34567 25')
        mock_stdin.seek(0)

        self.assertEqual(get_input(), [('12345', 12), ('23456', 1), ('34567', 25)])


class TestStr2Int(unittest.TestCase):
    pass


class TestInsertDecimalPoint(unittest.TestCase):
    pass


class TestSolve(unittest.TestCase):
    pass