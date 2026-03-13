from puzzle import get_blank_index, index_to_position, position_to_index, is_goal, goal
from solver import solve, reconstruct_path, display_path
from utils import print_board


def move(state, direction):
    blank = get_blank_index(state)
    row, col = index_to_position(blank)

    moves = {"w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1)}

    if direction not in moves:
        return state

    dy, dx = moves[direction]
    ny = row + dy
    nx = col + dx

    if ny < 0 or ny >= 3 or nx < 0 or nx >= 3:
        return state

    new_index = position_to_index(ny, nx)

    new_state = list(state)
    new_state[blank], new_state[new_index] = new_state[new_index], new_state[blank]

    return tuple(new_state)


def play_game(state, hint=True):
    while True:
        print_board(state)
        print()

        if is_goal(state):
            print("Solved!")
            break

        if hint:
            solution = solve(state)
            path = reconstruct_path(solution, goal)

            print("Moves needed:", len(path) - 1)

        print("Enter q to auto solve!")
        move_input = input("Move (w/a/s/d): ")

        if move_input == "q":
            display_path(state)
            break

        else:
            state = move(state, move_input)
