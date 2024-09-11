

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

    moves /= 2

    print(moves)


if __name__ == '__main__':
    while True:
        if input() == '0':
            break

        nums = [x for x in map(lambda x: int(x), input().split())]

        solve(nums)