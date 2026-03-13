from game import play_game
from puzzle import goal
from solver import solve, reconstruct_path
from utils import print_board, generate_random_state


def menu():
    while True:
        print("Welcome to SlidNum.")
        print("1. Play")
        print("2. Custom Board")
        print("3. Quit")
        menu_input = input("Choose (1-3): ")
        menu_input = int(menu_input)

        while menu_input < 1 and menu_input > 3:
            menu_input = input("Invalid! Choose (1-3):")

        if menu_input == 1:
            hint_input = input("Do you need hint? (0/1): ")

            hint_input = hint_input == 1
            state = generate_random_state(50)
            play_game(state, hint=hint_input)

        if menu_input == 2:
            print("This feature is currently not available!")
            continue

        if menu_input == 3:
            break


menu()
