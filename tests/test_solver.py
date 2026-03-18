from src.slidnum.solver import solve
from src.slidnum.puzzle import goal


def test_solver_goal():
    result = solve(goal)
    assert result is not None
