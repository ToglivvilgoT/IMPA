

def is_palindrome(num: int):
    return str(num) == str(reverse_int(num))


def reverse_int(num: int):
    str_num = str(num)
    str_num_reversed = str_num[::-1]

    return int(str_num_reversed)


def solve():
    num = int(input())

    iterations = 0

    while not is_palindrome(num):
        num_reversed = reverse_int(num)
        num += num_reversed

        iterations += 1

    print(iterations, num)


if __name__ == '__main__':
    tests = int(input())

    for _ in range(tests):
        solve()