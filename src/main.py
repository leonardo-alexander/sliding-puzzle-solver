from slidnum.cli import play_game
from slidnum.utils import generate_random_state
from slidnum.ui_pygame import run as run_pygame


def menu():
    while True:
        print("\n=== SlidNum ===")
        print("1. CLI Play")
        print("2. Pygame UI")
        print("3. Quit")

        try:
            choice = int(input("Choose: "))
        except ValueError:
            continue

        if choice == 1:
            state = generate_random_state(50)
            play_game(state, hint=True)

        elif choice == 2:
            run_pygame()

        elif choice == 3:
            break


if __name__ == "__main__":
    menu()
