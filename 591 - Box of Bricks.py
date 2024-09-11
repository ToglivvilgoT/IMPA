

def sum_list(nums):
    total = 0

    for num in nums:
        total += num

    return total


def solve(nums):
    target = sum_list(nums) // len(nums)

    moves = 0

    for pillar in nums:
        moves += abs(pillar - target)

    moves //= 2

    print(f"The minimum number of moves is {moves}.\n")


if __name__ == '__main__':
    test_case_id = 1
    while True:
        if input() == '0':
            break

        nums = [x for x in map(lambda x: int(x), input().split())]

        print(f"Set #{test_case_id}")

        solve(nums)

        test_case_id += 1