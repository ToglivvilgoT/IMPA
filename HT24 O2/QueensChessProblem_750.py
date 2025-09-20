t_vec2 = tuple[int, int]
t_board = set[t_vec2]


def get_input():
    test_cases = []

    inp_rows = int(input())
    
    for _ in range(inp_rows):
        input()
        test_cases.append(tuple(map(lambda n: int(n)-1, input().split())))

    return test_cases


def write_output(boards: list[t_board]):
    def sort_key(board: t_board):
        val = 0
        for queen_x, queen_y in board:
            val += (7-queen_y) * 8**(7-queen_x)

        return val

    boards.sort(key=sort_key, reverse=True)

    def board_to_print_row(board: t_board):
        print_row = [None for _ in range(8)]

        for x, y in board:
            print_row[x] = str(y+1)

        return print_row

    print('SOLN\tCOLUMN')
    print('#\t1 2 3 4 5 6 7 8')
    print()
    for i in range(len(boards)):
        print(f'{i+1}\t', end='')
        print(str.join(' ', board_to_print_row(boards[i])))


def place_queens(board: t_board) -> list[t_board]:
    """ returns a list of all valid 8 queen placements on board """
    def get_valid_queen_pos(board: set[t_vec2], col: int) -> set[int]:
        """ returns a set of all rows where a queen can be legally placed in col """
        invalid = set()

        for queen_x, queen_y in board:
            invalid.add(queen_y)
            
            diagonal_offset = abs(col - queen_x)
            invalid.add(queen_y + diagonal_offset)
            invalid.add(queen_y - diagonal_offset)

        return set(range(8)) - invalid

    found = False

    for col in range(8):
        empty = True

        for queen_x, queen_y in board:
            if col == queen_x:
                empty = False
                break

        if empty:
            found = True
            break

    if not found:
        return [board]
    
    possible_placements = []

    for row in get_valid_queen_pos(board, col):
        for placement in place_queens(board.union({(col, row)})):
            possible_placements.append(placement)

    return possible_placements


if __name__ == '__main__':
    test_cases = get_input()

    for i in range(len(test_cases)):
        write_output(place_queens({test_cases[i]}))