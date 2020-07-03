import pygame

from enum import Enum


class Color(Enum):
    WHITE = (0,0,0)
    BROWN = (102,51,0)
    GREEN = (50,204,0)
    RED = (204,0,0)
    YELLOW = (255,255,0)
    PINK = (255,153,255)
    PURPLE = (76,0,153)
    BLUE = (0,0,153)
    ORANGE = (255,158,0)


class Game_tile():
    def __init__(self,color):
        self.size = 64
        self.color = color
        self.occupied = False

def main():
    screen = setup_game()
    loop_game(screen)
    quit_game()


def setup_game():
    screen = pygame.display.set_mode((512,512))
    pygame.display.set_caption("Game")

    screen.fill(Color.WHITE.value)
    pygame.display.flip()
    return screen

def build_board():
    pass


def loop_game(screen):

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    screen.fill(Color.RED.value)
                if event.key == pygame.K_g:
                    screen.fill(Color.GREEN.value)
                if event.key == pygame.K_b:
                    screen.fill(Color.BLUE.value)
                pygame.display.flip()

def quit_game():
    pygame.quit()


if __name__ == '__main__':
    main()