

def get_biggest(lst: list):
    if isinstance(lst, int):
        return lst

    if len(lst) == 0:
        return None

    if len(lst) == 1:
        return get_biggest(lst[0])
    
    left = get_biggest(lst[0])
    right = get_biggest(lst[1:])

    if left == None:
        return right
    elif right == None:
        return left

    return max(left, right)


print(get_biggest([3, [4, [5, 11, -66], 12, []], 8, [4, 3]]))