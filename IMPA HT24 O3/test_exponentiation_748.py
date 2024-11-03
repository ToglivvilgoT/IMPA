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

        self.assertEqual(get_input(), [('123.45', 12)])

    @patch('sys.stdin', new_callable=io.StringIO)
    def test_multiple(self, mock_stdin: io.StringIO):
        mock_stdin.write('123.45 12\n23.456  1\n.34567 25')
        mock_stdin.seek(0)

        self.assertEqual(get_input(), [('123.45', 12), ('23.456', 1), ('.34567', 25)])


class TestStr2Int(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(str2int('123.45'), (12345, -2))

    def test_leading_zero(self):
        self.assertEqual(str2int('012.34'), (1234, -2))
        self.assertEqual(str2int('000.34'), (34, -2))
        self.assertEqual(str2int('00000.'), (0, 0))

    def test_trailing_zero(self):
        self.assertEqual(str2int('12.340'), (12340, -3))
        self.assertEqual(str2int('1.2000'), (12000, -4))
        self.assertEqual(str2int('.00000'), (0, -5))

    def test_leading_decimal(self):
        self.assertEqual(str2int('.12345'), (12345, -5))

    def test_trailing_decimal(self):
        self.assertEqual(str2int('12345.'), (12345, 0))

    def test_no_decimal(self):
        self.assertEqual(str2int('123456'), (123456, 0))


class TestInsertDecimalPoint(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(insert_decimal_point(123456, -5), '1.23456')
        self.assertEqual(insert_decimal_point(123456, -4), '12.3456')
        self.assertEqual(insert_decimal_point(123456, -3), '123.456')
        self.assertEqual(insert_decimal_point(123456, -2), '1234.56')
        self.assertEqual(insert_decimal_point(123456, -1), '12345.6')

    def test_leading_decimal(self):
        self.assertEqual(insert_decimal_point(123456, -6), '.123456')

    def test_trailing_decimal(self):
        self.assertEqual(insert_decimal_point(123456, 0), '123456')

    def test_leading_zeros(self):
        self.assertEqual(insert_decimal_point(123, -6), '.000123')

    def test_trailing_zeros(self):
        self.assertEqual(insert_decimal_point(123000, -3), '123')


class TestSolve(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solve('95.123', 12), '548815620517731830194541.899025343415715973535967221869852721')
        self.assertEqual(solve('0.4321', 20), '.00000005148554641076956121994511276767154838481760200726351203835429763013462401')
        self.assertEqual(solve('5.1234', 15), '43992025569.928573701266488041146654993318703707511666295476720493953024')
        self.assertEqual(solve('6.7592', 9), '29448126.764121021618164430206909037173276672')
        self.assertEqual(solve('98.999', 10), '90429072743629540498.107596019456651774561044010001')
        self.assertEqual(solve('1.0100', 12), '1.126825030131969720661201')

    def test_leading_decimal(self):
        self.assertEqual(solve('.12345', 5), '.0000' + str(12345**5))

    def test_trailing_decimal(self):
        self.assertEqual(solve('12345.', 5), str(12345**5))

    def test_leading_zeros(self):
        self.assertEqual(solve('0001.2', 5), '2.48832')
        self.assertEqual(solve('000.12', 5), '.0000248832')

    def test_trailing_zeros(self):
        self.assertEqual(solve('123.00', 5), str(123**5))


if __name__ == '__main__':
    unittest.main()