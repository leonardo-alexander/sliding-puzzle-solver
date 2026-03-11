from puzzle import goal
from solver import solve, reconstruct_path
from utils import print_board, generate_random_state

state = generate_random_state(steps=50)

came_from = solve(state)

if came_from is None:
    print("No solution")
else:
    path = reconstruct_path(came_from, goal)
    for step in path:
        print_board(step)
        print()
