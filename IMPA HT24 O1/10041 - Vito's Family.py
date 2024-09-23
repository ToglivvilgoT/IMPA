

def sort(lst: list[int]):
    if len(lst) < 2:
        return lst
    
    sorted = []
    
    split = len(lst) // 2
    part1 = sort(lst[0:split])
    part2 = sort(lst[split:])

    while part1 and part2:
        if part1 < part2:
            sorted.append(part1.pop(0))
        else:
            sorted.append(part2.pop(0))

    sorted += part1 + part2
                          
    return sorted


def sum_differance(lst: list[int], term: int):
    return sum(map(lambda x: abs(term - x), lst))


def solve(adresses: list[int]):
    adresses = sort(adresses)
    optimal_adress = adresses[len(adresses)//2]
    
    print(sum_differance(adresses, optimal_adress))


if __name__ == '__main__':
    test_cases = int(input())

    for test_case in range(test_cases):
        solve(list(map(lambda x: int(x), input().split()[1:])))