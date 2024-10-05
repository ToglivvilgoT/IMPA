from sys import stdin


def get_input():
    return stdin.read().split()


def solve(test_case: str):
    first, last = [], []
    current_index = len(test_case)

    next_home_press = test_case.rfind('[', 0, current_index)
    next_end_press = test_case.rfind(']', 0, current_index)

    while True:
        if next_home_press == next_end_press == -1:
            first.append(test_case[:current_index])
            break

        if next_home_press > next_end_press:
            first.append(test_case[next_home_press+1:current_index])
            current_index = next_home_press
            next_home_press = test_case.rfind('[', 0, current_index)
        else:
            last.append(test_case[next_end_press+1:current_index])
            current_index = next_end_press
            next_end_press = test_case.rfind(']', 0, current_index)

    last.reverse()
    print(str.join('', first + last))


if __name__ == '__main__':
    for test_case in get_input():
        solve(test_case)