import queue
import random
import time


t_board = list[list[int]]
t_que_item = tuple[int, tuple[t_board, int]]


def print_board(board: t_board):
    def number_to_print(n: int):
        if n < 10:
            return ' ' + str(n)
        else:
            return str(n)

    print('Board:')

    for y in range(4):
        print("\t[", end='')
        for x in range(4):
            print(number_to_print(board[y][x]), end='')

            if x != 3:
                print(',', end='')

            print(' ', end='')

        print("]")


def get_copy(board: t_board):
    copy = []

    for y in range(4):
        row = []
        for x in range(4):
            row.append(board[y][x])

        copy.append(row)

    return copy


def get_completed_board() -> t_board:
    return get_copy([
        [1,  2,  3,  4 ],
        [5,  6,  7,  8 ],
        [9,  10, 11, 12],
        [13, 14, 15, 0 ],
    ])


def is_solved(board: t_board):
    return board == get_completed_board()


def get_hash(board: t_board):
    hash_val = 0

    for y in range(4):
        for x in range(4):
            hash_val += board[y][x] * 16**(x + 4*y)

    return hash_val


def get_zero_pos(board: t_board):
    for y in range(4):
        for x in range(4):
            if board[y][x] == 0:
                return (x, y)
            
    raise ValueError('Invalid Board, has no "0"')


def get_moves(board: t_board) -> str:
    LEGAL_MOVES = {
        (0, 0): 'RD',
        (1, 0): 'LRD',
        (2, 0): 'LRD',
        (3, 0): 'LD',
        (0, 1): 'URD',
        (1, 1): 'ULRD',
        (2, 1): 'ULRD',
        (3, 1): 'ULD',
        (0, 2): 'URD',
        (1, 2): 'ULRD',
        (2, 2): 'ULRD',
        (3, 2): 'ULD',
        (0, 3): 'UR',
        (1, 3): 'ULR',
        (2, 3): 'ULR',
        (3, 3): 'UL',
    }
    return LEGAL_MOVES[get_zero_pos(board)]


def make_move(board: t_board, move: str):
    MOVE_TO_VECTOR = {
        'U': (0, -1),
        'L': (-1, 0),
        'R': (1, 0),
        'D': (0, 1),
    }

    dx, dy = MOVE_TO_VECTOR[move]
    zero_x, zero_y = get_zero_pos(board)

    board[zero_y][zero_x] = board[zero_y + dy][zero_x + dx]
    board[zero_y + dy][zero_x + dx] = 0


def get_inverse_moves(moves: str):
    INVERSED = {
        'U': 'D',
        'L': 'R',
        'R': 'L',
        'D': 'U',
    }
    inversed = ''
    
    for letter in moves:
        inversed += INVERSED[letter]

    return inversed


def make_random_move(board: t_board):
    moves = get_moves(board)

    move = moves[random.randrange(0, len(moves))]

    make_move(board, move)


def randomize_board(board: t_board, moves: int = 45):
    for _ in range(moves):
        make_random_move(board)


def get_score(board: t_board, moves: int, target_board: t_board = get_completed_board()):
    score = moves

    for y in range(4):
        for x in range(4):
            if board[y][x] == target_board[y][x]:
                score -= 3

            cur_y, cur_x = divmod(board[y][x]-1, 4)
            target_y, target_x = divmod(target_board[y][x]-1, 4)

            dx = abs(cur_x - target_x)
            dy = abs(cur_y - target_y)
            score += dx + dy
    
    return score


def solve(board: t_board, target_board: t_board = get_completed_board()):
    normal_que = queue.PriorityQueue()
    reversed_que = queue.PriorityQueue()

    normal_que.put((get_score(board, 0), (board, '')))
    reversed_que.put((get_score(target_board, 0, board), (target_board, '')))

    normal_checked: dict[int, (t_board, str)] = {}
    reversed_checked: dict[int, (t_board, str)] = {}

    normal_target = target_board
    reversed_target = board

    for _ in range(1000000):
        for que, same_checked, opposite_checked, target in (
                (normal_que, normal_checked, reversed_checked, normal_target), 
                (reversed_que, reversed_checked, normal_checked, reversed_target)
            ):
            prio, (board, performed_moves) = que.get(False)

            """if is_solved(board):
                print(f"solved in {performed_moves} moves")
                print(normal_que.qsize())
                return"""

            hashed_board = get_hash(board)
            if hashed_board in opposite_checked.keys():
                if normal_checked == same_checked:
                    solution = performed_moves + get_inverse_moves(opposite_checked[hashed_board][1][::-1])
                else:
                    solution = opposite_checked[hashed_board][1] + get_inverse_moves(performed_moves[::-1])

                print(f"Board solved in {len(solution)} moves")
                print(f"{solution}")
                return
            
            available_moves = get_moves(board)

            MAX_MOVES = 50
            if len(performed_moves)+1 > MAX_MOVES // 2:
                continue

            for available_move in available_moves:
                new_board = get_copy(board)
                make_move(new_board, available_move)

                hashed_board = get_hash(new_board)
                if hashed_board in same_checked.keys() and len(performed_moves)+1 >= len(same_checked[hashed_board][1]):
                    continue
                else:
                    same_checked[hashed_board] = (new_board, performed_moves + available_move)

                que.put((get_score(new_board, len(performed_moves)+1), (new_board, performed_moves + available_move)))

        
    print(normal_que.get(False)[1])


if __name__ == '__main__':
    board = get_completed_board()
    board = [
        [ 2,  0,  3,  4 ],
        [ 1,  7, 10, 15 ],
        [ 5,  9, 11,  8 ],
        [13,  6, 14, 12 ],
    ]
    board = [
        [ 2, 10,  7,  4 ],
        [ 5,  1,  3, 15 ],
        [ 9, 12, 11,  0 ],
        [13,  6, 14,  8 ],
    ]
    board = [
        [ 5,  3,  2,  1 ],
        [12,  9, 10,  7 ],
        [13, 11,  0,  4 ],
        [ 6,  8, 14, 15 ],
    ]
    randomize_board(board)
    board = [
        [ 5,  0,  9,  1 ],
        [ 2,  7,  3,  4 ],
        [12, 11, 14, 10 ],
        [13,  6,  8, 15 ],
    ] 

    print_board(board)

    start_time = time.time()
    solve(board)
    print(time.time() - start_time)