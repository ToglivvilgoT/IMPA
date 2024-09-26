

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
    next_grids = [grid]

    MAX_WIDTH = 15
    for depth in range(1, MAX_WIDTH**2+1):
        current_grids = next_grids
        next_grids = []

        for current_grid in current_grids:
            result = check_grid(current_grid, width)

            if isinstance(result, bool):
                if result:
                    return depth
                
            else:
                for next_grid in result:
                    next_grids.append(next_grid)


if __name__ == '__main__':
    print(solve(0b000100000, 3))
