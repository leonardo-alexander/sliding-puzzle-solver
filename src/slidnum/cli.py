from engine import move
from puzzle import is_goal, goal
from solver import reconstruct_path, display_path, solve
from utils import print_board


def play_game(state: tuple[int, ...], hint: bool = True):
    while True:
        print_board(state)
        print()

        if is_goal(state):
            print("Solved!")
            break

        solution, nodes = solve(state)
        if solution is None:
            print("No solution")
        else:
            path = reconstruct_path(solution, goal)

        if hint:
            print("Moves needed:", len(path) - 1)

        print(f"Moves: {len(path)-1}")
        print(f"Nodes expanded: {nodes}")

        print("Controls: W↑ A← S↓ D→ | Q = solve")
        move_input = input("Input: ")

        if move_input == "q":
            display_path(state)
            break

        else:
            state = move(state, move_input)
