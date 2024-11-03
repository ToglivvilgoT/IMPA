

def get_input():
    inp = []

    while True:
        line = input()

        if line == 'END':
            break
        else:
            inp.append(line)

    return inp


def solve(num: str):
    i = 1
    while True:
        next_num = len(num)

        if next_num == 1 and num == '1':
            print(i)
            return
        else:
            num = str(next_num)
            i += 1


if __name__ == '__main__':
    for test_case in get_input():
        solve(test_case)