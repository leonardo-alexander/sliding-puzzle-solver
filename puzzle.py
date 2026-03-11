def get_blank_index(state):
    return state.index(0)


def index_to_position(index):
    return index // 3, index % 3


def position_to_index(row, col):
    return 3 * row + col


def get_neighbors(state):
    neighbors = set()

    # Move UP, RIGHT, DOWN, LEFT
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    blank_index = get_blank_index(state)
    row, col = index_to_position(blank_index)

    for i in range(4):
        ny = row + dy[i]
        nx = col + dx[i]

        # easier validation with position instead of index
        if ny < 0 or ny >= 3 or nx < 0 or nx >= 3:
            continue

        new_index = position_to_index(ny, nx)
        new_state = list(state)

        new_state[new_index], new_state[blank_index] = (
            new_state[blank_index],
            new_state[new_index],
        )

        new_neigbour = tuple(new_state)
        neighbors.add(new_neigbour)

    return neighbors


def is_goal(state):
    return state == goal

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)