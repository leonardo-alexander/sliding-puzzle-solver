from slidnum.utils import generate_random_state
from slidnum.solver import solve


def run_benchmark(n=10):
    for i in range(n):
        state = generate_random_state(50)
        _, nodes = solve(state)
        print(f"Test {i}: {nodes} nodes")
