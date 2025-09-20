

def solve():
    num1, num2 = map(lambda x: int(x), input().split())

    if num1 < num2:
        print('<')
    elif num1 > num2:
        print('>')
    else:
        print('=')


if __name__ == '__main__':
    tests = int(input())

    for _ in range(tests):
        solve()