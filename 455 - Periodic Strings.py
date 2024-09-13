

def has_period(text: str, period: int):
    if len(text) % period != 0:
        return False
    
    for i in range(len(text)):
        if text[i] != text[i % period]:
            return False
        
    return True


def solve(inp: str):
    for period in range(1, len(inp) + 1):
        if has_period(inp, period):
            print(period)
            return


if __name__ == '__main__':
    test_cases = int(input())

    for test_case in range(test_cases):
        input()
        
        solve(input())

        if test_case != test_cases - 1:
            print()