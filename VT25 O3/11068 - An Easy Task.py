def get_input():
    inp = []
    while True:
        line1 = list(map(int, input().split()))
        line2 = list(map(int, input().split()))
        if line1 == line2 == [0, 0, 0]:
            break
        else:
            inp.append((line1, line2))
    return inp


def linalg_solvable(line1, line2):
    a1, b1, c1 = line1
    a2, b2, c2 = line2
    if b1 != 0 and b2 != 0:
        return a1 / b1 != a2 / b2
    else:
        return b1 != b2 and a1 != b1


def linalg_solve(line1, line2):
    a1, b1, c1 = line1
    a2, b2, c2 = line2
    t = c1 * b2 / b1 - c2
    n = b2 * a1 / b1 - a2
    x = t / n
    y = (c1 - a1 * x) / b1
    return x, y
    

def solve(lines):
    line1, line2 = lines
    if linalg_solvable(line1, line2):
        a, b = linalg_solve(line1, line2)
        return f'The fixed point is at {a:.2f} {b:.2f}.'
    else:
        return 'No fixed point exists.'


if __name__ == '__main__':
    for inp in get_input():
        print(solve(inp))