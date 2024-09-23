

def solve(inp: list[tuple[str, int]]):
    best_urls = []
    best_relevance = -1

    for url, relevance in inp:
        if relevance == best_relevance:
            best_urls.append(url)

        elif relevance > best_relevance:
            best_relevance = relevance
            best_urls = [url]

    for url in best_urls:
        print(url)


def get_input():
    inp = []

    INPUT_LINES = 10
    for _ in range(INPUT_LINES):
        url, relevance = input().split()
        relevance = int(relevance)
        inp.append((url, relevance))

    return inp


if __name__ == '__main__':
    test_cases = int(input())

    for test_case in range(1, test_cases + 1):
        print(f'Case #{test_case}:')
        solve(get_input())