import pygame
import sys
import itertools

from slidnum.engine import move
from slidnum.utils import generate_random_state
from slidnum.puzzle import is_goal, goal
from slidnum.solver import solve, reconstruct_path

SIZE = 3
TILE_SIZE = 120
WIDTH = HEIGHT = SIZE * TILE_SIZE + 60  # extra space for text

WHITE = (255, 255, 255)
BLUE = (50, 150, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SlidNum")
font = pygame.font.Font(None, 40)

state = generate_random_state(50)


def draw_board(state):
    for i, j in itertools.product(range(SIZE), range(SIZE)):
        tile = state[SIZE * i + j]
        rect = pygame.Rect(j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE)

        if tile == 0:
            pygame.draw.rect(screen, GRAY, rect)
        else:
            pygame.draw.rect(screen, BLUE, rect)
            text = font.render(str(tile), True, WHITE)
            screen.blit(text, text.get_rect(center=rect.center))

        pygame.draw.rect(screen, BLACK, rect, 2)


def draw_text(text):
    label = font.render(text, True, BLACK)
    screen.blit(label, (10, HEIGHT - 40))


def handle_input(event, state):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            return move(state, "w")
        elif event.key == pygame.K_s:
            return move(state, "s")
        elif event.key == pygame.K_a:
            return move(state, "a")
        elif event.key == pygame.K_d:
            return move(state, "d")

        elif event.key == pygame.K_r:
            return generate_random_state(50)

        elif event.key == pygame.K_h:
            if result := solve(state):
                came_from, _ = result
                path = reconstruct_path(came_from, goal)
                if len(path) > 1:
                    return path[1]

    return state


def run():
    global state

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            state = handle_input(event, state)

        screen.fill(WHITE)
        draw_board(state)

        if is_goal(state):
            draw_text("Solved! Press R to restart")
        else:
            draw_text("WASD move | H hint | R restart")

        pygame.display.update()
