import sys


def get_input():
    inp = sys.stdin.read().splitlines()
    return inp[1:]


def solve(path: str):
    stack = [path[0]]
    connections = {path[0]: 0}

    for fountain in path[1:]:
        if stack[-1] == fountain:
            stack.pop()
        else:
            connections[stack[-1]] += 1
            connections[fountain] = 1
            stack.append(fountain)

    return connections


def print_dict(dic: dict):
    for key in sorted(dic.keys()):
        print(f'{key} = {dic[key]}')


if __name__ == '__main__':
    test_cases = get_input()

    for i in range(len(test_cases)):
        print(f'Case {i+1}')
        print_dict(solve(test_cases[i]))