

def get_input() -> list[tuple[int, int]]:
    inp = []

    while True:
        num_range = tuple(map(int, input().split()))

        if num_range == (0, 0):
            break
        else:
            inp.append(num_range)

    return inp


_lookup_table: dict[int, int] = {1: 3, 2: 1}
def lookup_add(path: list[int]):
    global _lookup_table

    path.reverse()
    start_len = _lookup_table[path[0]]

    for i in range(len(path)):
        _lookup_table[path[i]] = start_len + i


def get_sequence_len(start: int):
    path = [start]

    while True:
        if path[-1] in _lookup_table.keys():
            lookup_add(path)
            return _lookup_table[start]

        if path[-1]%2 == 0:
            path.append(path[-1] // 2)
        else:
            path.append(path[-1]*3 + 1)


def solve(num_range: tuple[int, int]):
    seq_lengths: list[tuple[int, int]] = []

    start, end = min(num_range), max(num_range) + 1

    for num in range(start, end):
        seq_lengths.append((num, get_sequence_len(num)))

    seq_lengths.sort(key=lambda x: x[1], reverse=True)

    print(f'Between {start} and {end-1}, {seq_lengths[0][0]} generates the longest sequence of {seq_lengths[0][1]} values.') 


if __name__ == '__main__':
    for test_case in get_input():
        solve(test_case)