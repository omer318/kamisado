import pygame

from enum import Enum


class Color(Enum):
    RED = (0,0,255)
    GREEN = (102,204,0)
    BLUE = (0,0,153)


class Game_tile():
    def __init__(self,color):
        self.size = 64
        self.color = color

def main():
    setup_game()
    loop_game()
    quit_game()


def setup_game():
    screen = pygame.display.set_mode((512,512))
    pygame.display.set_caption("Game")

    screen.fill(Color.BLUE.value)
    pygame.display.flip()


def loop_game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

def quit_game():
    pygame.quit()


if __name__ == '__main__':
    main()