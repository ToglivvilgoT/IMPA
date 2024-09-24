import sys

def get_input():
    return sys.stdin.read().split()


def solve(phone_number: str):
    FROM = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    TO =   '22233344455566677778889999'
    TRANS = str.maketrans(FROM, TO)

    print(phone_number.translate(TRANS))


if __name__ == '__main__':
    inp = get_input()

    for line in inp:
        solve(line)