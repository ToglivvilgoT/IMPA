

def get_result(result: str):
    if result == '1' or result == '4' or result == '78':
        return '+'
    
    elif result[-2:] == '35':
        return '-'
    
    elif result[:3] == '190':
        return '?'
    
    else:
        return '*'


def solve(inp: str):
    print(get_result(inp))


if __name__ == '__main__':
    test_cases = int(input())

    for _ in range(test_cases):
        solve(input())