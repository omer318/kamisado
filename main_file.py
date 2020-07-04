import pygame
import time

from enum import Enum


class Color(Enum):
    WHITE = (255,255,255)
    BROWN = (102,51,0)
    GREEN = (50,175,0)
    RED = (175,0,0)
    YELLOW = (225,225,0)
    PINK = (255,125,125)
    PURPLE = (153,0,153)
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
                pygame.display.flip()
        for color in Color:
            screen.fill(color.value)
            pygame.display.flip()
            time.sleep(0.5)

def quit_game():
    pygame.quit()


if __name__ == '__main__':
    main()