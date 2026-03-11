from puzzle import index_to_position


def manhattan_distance(state):
    total = 0

    for index, tile in enumerate(state):
        if tile == 0:
            continue

        row, col = index_to_position(index)
        goal_row, goal_col = index_to_position(tile - 1)

        total += abs(row - goal_row) + abs(col - goal_col)

    return total


def linear_conflict(state):
    conflicts = 0

    # check rows
    for row in range(3):
        tiles = []

        for col in range(3):
            tile = state[3 * row + col]

            if tile != 0 and (tile - 1) // 3 == row:
                tiles.append(tile)

        for i in range(len(tiles)):
            for j in range(i + 1, len(tiles)):
                if (tiles[i] - 1) % 3 > (tiles[j] - 1) % 3:
                    conflicts += 1

    # check columns
    for col in range(3):
        tiles = []

        for row in range(3):
            tile = state[3 * row + col]

            if tile != 0 and (tile - 1) % 3 == col:
                tiles.append(tile)

        for i in range(len(tiles)):
            for j in range(i + 1, len(tiles)):
                if (tiles[i] - 1) // 3 > (tiles[j] - 1) // 3:
                    conflicts += 1

    return conflicts


def heuristic(state):
    return manhattan_distance(state) + 2 * linear_conflict(state)
