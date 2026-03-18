def get_blank_index(state: tuple[int, ...]) -> int:
    return state.index(0)


def index_to_position(index: int) -> tuple[int, ...]:
    return index // 3, index % 3


def position_to_index(row: int, col: int) -> int:
    return 3 * row + col


def get_neighbors(state: tuple[int, ...]) -> set:
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


def is_goal(state: tuple[int, ...]) -> bool:
    return state == goal


def is_solvable(state: tuple[int, ...]) -> bool:
    inv = 0
    arr = [x for x in state if x != 0]

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inv += 1

    return inv % 2 == 0


goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
