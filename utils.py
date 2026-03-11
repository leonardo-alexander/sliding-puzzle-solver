import random
from puzzle import get_neighbors, goal


def print_board(state):
    for i in range(3):
        for j in range(3):
            tile = state[3 * i + j]
            print("-" if tile == 0 else tile, end=" ")
        print()


def generate_random_state(steps=50):
    state = goal

    for _ in range(steps):
        neighbors = list(get_neighbors(state))
        state = random.choice(neighbors)

    return state
