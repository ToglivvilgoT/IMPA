

def solve(num1, num2):
    print(abs(num1 - num2))


if __name__ == '__main__':
    try:
        while True:
            test_case = input()
            if not test_case:
                break

            num1, num2 = map(lambda x: int(x), test_case.split())
            solve(num1, num2)

    except EOFError:
        exit(0)