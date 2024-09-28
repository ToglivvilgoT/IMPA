import sys


def matrix_to_int(grid_matrix: list[list[int]], width):
    """ converts a matrix represented grid to an integer representation """
    grid_int = 0

    for y in range(width):
        for x in range(width):
            grid_int += grid_matrix[y][x] * 2**x * 2**(3*y)

    return grid_int


def get_input():
    """
    reads input and returns it as a list of test cases
    where each test case is a tuple containing grid and width
    """
    test_cases: list[tuple[int, int]] = []

    inp = sys.stdin.read().splitlines()

    i = 1
    while i < len(inp):
        width = int(inp[i])

        grid_matrix = []
        for i in range(i + 1, i + 1 + width):
            grid_matrix.append([int(n) for n in inp[i].split()])

        test_cases.append((matrix_to_int(grid_matrix, width), width))

        i += 1

    return test_cases



def is_inbound(x: int, y: int, width: int):
    return x >= 0 and y >= 0 and x < width and y < width


def coords2grid(x: int, y: int, width: int) -> int:
    return 2**x * 2**(width * y)


def check_neighbours(grid: int, x: int, y: int, width: int):
    zeros = []
    parity = 0

    for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
        new_x, new_y = x + dx, y + dy

        if is_inbound(new_x, new_y, width):
            if (grid & coords2grid(new_x, new_y, width)) == 0:
                zeros.append((new_x, new_y))
            else:
                parity += 1

    return parity, zeros


def check_grid(grid: int, width: int):
    new_grids = set()

    for y in range(width):
        for x in range(width):
            parity, zeros = check_neighbours(grid, x, y, width)

            if parity % 2 == 1:
                if len(zeros) == 0:
                    return False
                
                for change_x, change_y in zeros:
                    new_grid = grid + coords2grid(change_x, change_y, width)
                    new_grids.add(new_grid)
            
    if not new_grids:
        return True
    else:
        return new_grids


def solve(grid: int, width: int):
    next_grids = {grid}

    MAX_WIDTH = 15
    for depth in range(MAX_WIDTH**2):
        current_grids = next_grids
        next_grids = set()

        for current_grid in current_grids:
            result = check_grid(current_grid, width)

            if isinstance(result, bool):
                if result:
                    return depth
                
            else:
                for next_grid in result:
                    next_grids.add(next_grid)
    
    return -1


def main():
    inps = get_input()

    for i in range(len(inps)):
        grid, width = inps[i]

        print(f'Case {i+1}: {solve(grid, width)}')


if __name__ == '__main__':
    main()
