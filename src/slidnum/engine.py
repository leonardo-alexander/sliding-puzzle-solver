from puzzle import get_blank_index, index_to_position, position_to_index


def move(state: tuple[int, ...], direction: str) -> tuple[int, ...]:
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
