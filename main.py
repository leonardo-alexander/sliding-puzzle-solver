import heapq


def print_board(state):
    for i in range(3):
        for j in range(3):
            tile = state[3 * i + j]
            print("-" if tile == 0 else tile, end=" ")
        print()


def get_blank_index(state):
    return state.index(0)


def index_to_position(index):
    return index // 3, index % 3


def position_to_index(row, col):
    return 3 * row + col


def get_neighbours(state):
    neighbours = set()

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
        neighbours.add(new_neigbour)

    return neighbours


def is_goal(state):
    return state == goal


def manhattan_distance(state):
    total = 0

    for index, tile in enumerate(state):
        if tile == 0:
            continue

        row, col = index_to_position(index)
        goal_row, goal_col = index_to_position(tile - 1)

        total += abs(row - goal_row) + abs(col - goal_col)

    return total


def change_state(state):
    min_distance = 1000
    best_neighbour = state

    for neighbor in get_neighbours(state):
        neighbor_distance = manhattan_distance(neighbor)

        if neighbor_distance < min_distance:
            min_distance = neighbor_distance
            best_neighbour = neighbor

    return best_neighbour


def solve(state):
    print("Initial board")
    print_board(state)

    g_score = {state: 0}
    open_set = []

    heapq.heappush(open_set, (manhattan_distance(state), 0, state))

    while open_set:
        current_f, current_g, current_state = heapq.heappop(open_set)

        if current_g > g_score.get(current_state, float("inf")):
            continue

        # print("g:", current_g)
        # print("f:", current_f)
        # print_board(current_state)

        if is_goal(current_state):
            return

        for neighbour in get_neighbours(current_state):
            tentative_g = current_g + 1

            if tentative_g < g_score.get(neighbour, float("inf")):
                g_score[neighbour] = tentative_g
                f_score = tentative_g + manhattan_distance(neighbour)

                heapq.heappush(
                    open_set,
                    (
                        f_score,
                        tentative_g,
                        neighbour,
                    ),
                )


goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
state = (1, 2, 4, 3, 5, 6, 7, 8, 0)

solve(state)
