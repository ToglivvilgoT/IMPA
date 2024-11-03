import sys


def get_input() -> list[tuple[str, int]]:
    """ returns a list of all rows in the input split into two parts """
    input_lines = sys.stdin.readlines()
    parsed_input_lines = map(lambda x: tuple(x.split(' ')), input_lines)
    return list(parsed_input_lines)


def str2int(number: str) -> tuple[int, int]:
    """ turns a string into a number in the format n * 10^k 
    returns (n, k) """
    whole, decimal = number.split('.')

    decimal_point = -len(decimal)
    converted_number = int(whole + decimal)
    
    return converted_number, decimal_point


def insert_decimal_point(number: int, decimal_point: int) -> str:
    """ inserts the decimal point into the number and return result as a string """
    str_number = str(number)

    leading_zeros = decimal_point - len(str_number)

    str_number = leading_zeros * '0' + str_number

    return str.join('.', [str_number[:-decimal_point], str_number[-decimal_point:]])


def solve(number: str, exponent: int) -> None:
    """ solves the problem for one test case and prints out the answer """
    parsed_number, decimal_point = str2int(number)

    final_number = parsed_number ** exponent
    final_decimal_point = decimal_point * exponent

    print(insert_decimal_point(final_number, final_decimal_point))


if __name__ == '__main__':
    for number, exponent in get_input():
        solve(number, exponent)