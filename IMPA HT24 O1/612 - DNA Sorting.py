

def get_sortedness(dna_seq: str):
    sortedness = 0

    times_occured = {
        'A': 0,
        'C': 0,
        'G': 0,
        'T': 0,
    }

    for i in range(len(dna_seq) - 1, -1, -1):
        letter = dna_seq[i]
        times_occured[letter] += 1

        for key, value in times_occured.items():
            if ord(letter) > ord(key):
                sortedness += value

    return sortedness


def solve(inp: list[str]):
    sortedness_dna = []

    for dna_seq in inp:
        sortedness_dna.append((get_sortedness(dna_seq), dna_seq))

    while sortedness_dna:
        best_index = -1
        best_sortedness = 9999999999999

        for i in range(len(sortedness_dna)):
            sortedness = sortedness_dna[i][0]

            if sortedness < best_sortedness:
                best_sortedness = sortedness
                best_index = i

        print(sortedness_dna.pop(best_index)[1])

    


def get_input():
    dna_len, dna_amount = map(lambda x: int(x), input().split())

    inp = []
    for _ in range(dna_amount):
        inp.append(input())

    return inp


if __name__ == '__main__':
    test_cases = int(input())

    for test_case in range(test_cases):
        input()
        inp = get_input()
        solve(inp)

        # print empty line between test cases (dont print after last test case)
        if test_case != test_cases - 1:
            print()