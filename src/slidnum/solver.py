import heapq
from heuristics import heuristic
from puzzle import get_neighbors, is_goal, goal
from utils import print_board


def solve(state: tuple[int, ...]):
    g_score = {state: 0}
    open_set = []
    came_from = {}
    nodes_expanded = 0

    heapq.heappush(open_set, (heuristic(state), 0, state))

    while open_set:
        current_f, current_g, current_state = heapq.heappop(open_set)

        if current_g > g_score.get(current_state, float("inf")):
            continue

        nodes_expanded += 1

        if is_goal(current_state):
            return came_from, nodes_expanded

        for neighbor in get_neighbors(current_state):
            tentative_g = current_g + 1

            if tentative_g < g_score.get(neighbor, float("inf")):
                came_from[neighbor] = current_state
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor)

                heapq.heappush(
                    open_set,
                    (
                        f_score,
                        tentative_g,
                        neighbor,
                    ),
                )

    return None


def reconstruct_path(
    came_from: dict, current: tuple[int, ...]
) -> list[tuple[int, ...]]:
    path = [current]

    while current in came_from:
        current = came_from[current]
        path.append(current)

    path.reverse()
    return path


def display_path(state: tuple[int, ...]):
    came_from = solve(state)

    print("AUTO SOLVING!")

    if came_from is None:
        print("No solution")
    else:
        path = reconstruct_path(came_from, goal)
        for i in range(len(path)):
            print("Move", i, ":")
            print_board(path[i])
            print()
